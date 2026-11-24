#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$(readlink -f "$0")")/.."
exec 9>/opt/adsblock-filter/update.lock
flock -n 9 || { echo "Update already running"; exit 1; }
# Existing VPS GitHub CLI authentication; never store tokens in the repository.
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' pull --ff-only origin main
python3 worker/update.py
git add -- filters/AdGuard_Desktop.txt filters/AdGuard_Android.txt
if ! git diff --cached --quiet; then
  git commit -m "chore(filters): refresh AdGuard subscriptions"
fi
git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push origin HEAD:main
