#!/usr/bin/env python3
"""Build two AdGuard subscription files; publish only after all sources validate."""
import concurrent.futures as cf
import datetime as dt
import hashlib
import os
from pathlib import Path
import re
import sys
import tempfile
import time
import urllib.request
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source/List_Filter_ADS.txt"
LOCAL = "https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/refs/heads/main/source/myfilter.txt"
FILES = {"desktop": "AdGuard_Desktop.txt", "android": "AdGuard_Android.txt"}
MAX_BYTES = 40 * 1024 * 1024
DOMAIN = re.compile(r"(?=.{1,253}$)(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", re.I)
HOST = re.compile(r"^(?:0\.0\.0\.0|127\.0\.0\.1|::|::1)\s+(\S+)(?:\s+#.*)?$")
TRUSTED = re.compile(r"#(?:@)?%#(?!//scriptlet\()|#(?:@)?%#//scriptlet\(\s*['\"]trusted-", re.I)
UBO = re.compile(r"#(?:@)?#\+js\(|#(?:@)?\$#.*\babort-on-", re.I)

def sources():
    groups = {k: [] for k in ("common", *FILES)}
    section = "common"
    for line in SOURCE.read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1]
            if section not in groups:
                raise ValueError("Unknown target: " + section)
            continue
        parsed = urlsplit(line)
        if parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.query or parsed.fragment:
            raise ValueError("Only public HTTPS source URLs without credentials or query parameters are allowed")
        if "/vip/" in parsed.path.lower() or "/premium/" in parsed.path.lower():
            raise ValueError("Premium sources may not be redistributed")
        if line not in groups[section]:
            groups[section].append(line)
    targets = {k: list(dict.fromkeys(groups["common"] + groups[k])) for k in FILES}
    if any(not urls for urls in targets.values()):
        raise ValueError("Empty source group")
    return targets

def parse(raw):
    if "\x00" in raw or raw.lstrip().lower().startswith(("<html", "<!doctype", "<?xml")):
        raise ValueError("Not a filter text")
    result = []
    skipped = 0
    for item in raw.splitlines():
        line = item.strip()
        if not line or line.startswith("["):
            continue
        if line.startswith("!"):
            if re.match(r"^!#(?:if|else|endif|include)\b", line):
                raise ValueError("Unresolved upstream preprocessor directive")
            continue
        if TRUSTED.search(line) or UBO.search(line):
            skipped += 1
            continue
        if line.startswith("#") and not line.startswith(("##", "#@#", "#?#", "#$#", "#%#", "#@?#", "#@$#", "#@%#")):
            continue
        host = HOST.fullmatch(line)
        if host:
            name = host.group(1)
            if not DOMAIN.fullmatch(name):
                continue
            line = "||" + name.lower() + "^"
        elif DOMAIN.fullmatch(line) and "." in line:
            line = "||" + line.lower() + "^"
        result.append(line)
    return result, skipped

def download(url):
    last = None
    for attempt in range(3):
        try:
            if url == LOCAL:
                data = (ROOT / "source/myfilter.txt").read_bytes()
            else:
                req = urllib.request.Request(url, headers={"User-Agent": "AdsBlock-Filter/1.0"})
                with urllib.request.urlopen(req, timeout=40) as response:
                    if urlsplit(response.geturl()).scheme != "https":
                        raise ValueError("Insecure redirect")
                    data = response.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError("Source exceeds size limit")
            raw = data.decode("utf-8-sig")
            rules, skipped = parse(raw)
            if len(rules) < (1 if url == LOCAL else 100):
                raise ValueError("Too few rules")
            return rules, skipped
        except Exception as e:
            last = e
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Source failed: {url}: {last}")

def make_body(urls, fetched):
    seen = set()
    rules = []
    total = 0
    for url in urls:
        for rule in fetched[url][0]:
            total += 1
            if rule not in seen:
                seen.add(rule)
                rules.append(rule)
    return rules, total - len(rules)

def build():
    targets = sources()
    urls = list(dict.fromkeys(u for group in targets.values() for u in group))
    fetched = {}
    with cf.ThreadPoolExecutor(max_workers=6) as pool:
        for url, future in [(u, pool.submit(download, u)) for u in urls]:
            fetched[url] = future.result()
            print(f"source {len(fetched[url][0])} rules; excluded {fetched[url][1]}: {url}", flush=True)
    outputs = {}
    for target, name in FILES.items():
        rules, duplicates = make_body(targets[target], fetched)
        if len(rules) < 1000:
            raise ValueError(f"Too few total rules for {target}")
        path = ROOT / "filters" / name
        old = path.read_text(encoding="utf-8") if path.exists() else ""
        body = "\n".join(rules) + "\n"
        digest = hashlib.sha256(("\n".join(targets[target]) + "\n" + body).encode()).hexdigest()
        if old:
            old_rules = sum(bool(l) and not l.startswith(("!", "[")) for l in old.splitlines())
            if len(rules) < old_rules * 0.75:
                raise ValueError(f"Suspicious rule count drop for {target}: {old_rules} -> {len(rules)}")
        print(f"{target}: {len(rules)} unique, {duplicates} duplicates removed", flush=True)
        if f"! Content-SHA256: {digest}\n" in old and old.split("! End header\n", 1)[-1] == body:
            continue
        now = dt.datetime.now(dt.timezone.utc)
        header = [
            "[Adblock Plus 2.0]", f"! Title: Lowji194 - AdGuard {target.title()}",
            f"! Version: {now:%Y%m%d%H%M%S}", f"! Last modified: {now:%Y-%m-%dT%H:%M:%SZ}",
            "! Expires: 7 days", "! Homepage: https://github.com/lowji194/AdsBlock-Filter",
            "! License: GPL-3.0; upstream attribution: see README.md",
            f"! Rules: {len(rules)}", f"! Content-SHA256: {digest}",
            *("! Source: " + u for u in targets[target]), "! End header"
        ]
        outputs[path] = "\n".join(header) + "\n" + body
    for path, data in outputs.items():
        path.parent.mkdir(exist_ok=True)
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", newline="\n", dir=path.parent, delete=False) as f:
            f.write(data)
            temp = f.name
        os.chmod(temp, 0o644)
        os.replace(temp, path)
    print(f"{len(outputs)} file(s) changed", flush=True)

if __name__ == "__main__":
    try:
        build()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
