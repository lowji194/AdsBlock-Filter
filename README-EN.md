[![🇻🇳 Tiếng Việt](https://img.shields.io/badge/Ngôn_ngữ-Tiếng_Việt-red?style=for-the-badge&logo=Google%20Translate)](README.md)
# **🔥Ad Filter By Loi Nguyen🔥**

This is an advanced ad filter developed by **Nguyen The Loi**. It combines public filter sources into separate subscriptions optimized for **AdGuard Browser Extension (Desktop)** and **AdGuard for Android**, helping block ads, reduce tracking, and improve your browsing experience.

---

## 📅 **Update Information**

- **Website**: [Lowji194](https://lowji194.github.io)
- **For**: AdGuard Browser Extension / AdGuard for Android
- **Author**: Nguyen The Loi
- **Description**: Ad blocking and privacy protection
- **Updates**: Automatically every 7 days, Monday at 03:00 (UTC+7)
- **Source code**: [GitHub](https://github.com/lowji194/AdsBlock-Filter)
- **Phone**: 0963 159 294
- **Facebook**: [Nguyen The Loi](https://www.facebook.com/Lowji194/)

---

## 🚀 **User Guide**

Two separate filter subscriptions are available for desktop browsers and Android. Install AdGuard and subscribe to the URL matching your device.

### 1. **Install AdGuard**

- 🖥️ **AdGuard Browser Extension (Desktop)**: Install from the [Chrome Web Store](https://chromewebstore.google.com/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg), [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/adguard-adblocker/), or the [official download page](https://adguard.com/en/adguard-browser-extension/overview.html).
- 📱 **AdGuard for Android**: Download the full application from the [official AdGuard website](https://adguard.com/en/adguard-android/overview.html).

### 2. **Add Filters to AdGuard**

#### 🖥️ AdGuard Browser Extension — Desktop

1. Click the **AdGuard** icon in your browser.
2. Open **Settings** → **Filters**.
3. Open **Custom**, select **Add custom filter**, and enter the following URL:

```text
https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt
```

[![Desktop](https://img.shields.io/badge/AdGuard-Desktop-4285F4?style=for-the-badge&logo=adguard&logoColor=white)](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt)

#### 📱 AdGuard for Android — Mobile

1. Open **AdGuard** and go to **Protection**.
2. Select **Ad blocking** → **Filters** → **Custom filters**.
3. Select **Add custom filter** and enter the following URL:

```text
https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt
```

[![Android](https://img.shields.io/badge/AdGuard-Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt)

### 3. **Enable the Filter**

**Desktop (Chrome / Edge / Firefox):** Lowji194 Desktop is a lightweight supplement. Enable **AdGuard Base filter**, **AdGuard Tracking Protection filter** (or EasyPrivacy), **AdGuard Quick Fixes filter** when available, and the built-in **uBlock Origin – Badware risks** security filter if available. Do not import these large lists again through custom URLs. ABPVN is already included in Lowji194 Desktop; avoid enabling duplicate ABPVN lists.

**Android:** The full aggregate is unchanged and is not subject to the Desktop budget.

After adding the URL, enable the filter and check your protection status in AdGuard. You can update, enable, or disable it at any time in the settings.

> **Note:** Add only the URL matching your device. On Android, use content filters, not DNS filters. HTTPS filtering depends on the application and device configuration. Do not mark this list as trusted. Chrome/Edge Manifest V3 shares dynamic and regex quotas. The worker caps Desktop at 3,000 raw rules to leave headroom; the actual converted DNR rule count may differ. See [AdGuard MV3 documentation](https://adguard.com/kb/adguard-browser-extension/mv3-version/). Replace any legacy subscription URLs with the new ones above.

---

## ⚙️ **Technical Information**

These filters help block ads, pop-ups, tracking services, and some other unwanted content. The automated worker combines sources, normalizes rules, removes exact duplicates, and builds platform-specific subscriptions.

### **Filter Sources**

| Source | Desktop | Android |
|---|:---:|:---:|
| [AdGuard Base / EasyList](https://github.com/AdguardTeam/AdguardFilters) | Built-in | ✅ |
| [EasyPrivacy](https://github.com/easylist/easylist) | Built-in | ✅ |
| [ABPVN List](https://github.com/abpvn/abpvn) | ✅ | ✅ |
| [uBlock Badware risks (AdGuard-optimized)](https://github.com/uBlockOrigin/uAssets) | Built-in | ✅ |
| [Lowji194 custom rules](source/myfilter.txt) | ✅ | ✅ |
| [AdGuard Mobile Ads](https://github.com/AdguardTeam/AdguardFilters) | — | ✅ |

Entries marked "Built-in" are recommended extension filters, not included in the Desktop subscription.

Source configuration: [List_Filter_ADS.txt](source/List_Filter_ADS.txt). AdGuard-compatible variants are used; unauthorized premium lists, DNS-only aggregates, and the legacy URLhaus format are excluded.

### **Automatic Updates**

- **Schedule:** Every 7 days (Monday at 03:00, UTC+7).
- **System:** Python worker and systemd timer on a VPS.
- **Desktop budget:** Maximum 3,000 raw rules, prioritizing ABPVN and local rules. If the budget is exceeded, publishing stops rather than arbitrarily truncating rules or exceptions. Android is not subject to this policy.
- **Process:** Download → validate → deduplicate → build two filters → publish changes to GitHub.
- **Safety:** Up to three attempts per source; failed downloads or unusually large rule-count drops preserve the previously published version.
- **Source code:** [Worker](worker/) · [Systemd](systemd/).

On the current VPS, systemd units reside under /usr/local/lib/systemd/system/ with a timers.target dependency because /etc is read-only. The timer is active; reboot persistence has not been tested. Manual operation:

```bash
systemctl start adsblock-filter.service
systemctl list-timers adsblock-filter.timer
journalctl -u adsblock-filter.service -n 50 --no-pager
```

### **License and Compatibility**

The modified aggregate and worker are distributed under [GPL-3.0](LICENSE). Upstream copyright and license terms apply (including the license options offered by EasyList/EasyPrivacy). Source URLs are recorded in each filter header.

This independent project is not an official AdGuard filter. Not intended for AdGuard Home or Android Private DNS. The worker and raw URLs have been verified; actual device imports have not been tested. No filter guarantees blocking every ad or replaces dedicated malware protection.

---

## 📌 **Contact**

If you encounter any problems or want to contribute to the project, you can contact me via:

- **Phone**: 0963 159 294
- **Facebook**: [Lowji194](https://www.facebook.com/Lowji194/)

---

## ☕ **Support me with a coffee**
<p align="center">
  <img src="https://theloi.io.vn/pay/QR.png?text=QR+Code" alt="Mời cà phê" width="240" />
</p>
