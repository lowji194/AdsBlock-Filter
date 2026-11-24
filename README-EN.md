# AdsBlock Filter — Lowji194

[Tiếng Việt](README.md)

Two public-source AdGuard subscriptions, rebuilt weekly:

| Platform | Subscription |
|---|---|
| Desktop browser extension | [AdGuard_Desktop.txt](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt) |
| AdGuard for Android | [AdGuard_Android.txt](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt) |

Add only the matching URL under Custom filters in AdGuard. On Android use content filtering, not DNS filtering. These are not AdGuard Home lists. HTTPS filtering is subject to device/app limitations. Chrome Manifest V3 has rule limits; not every rule may be applied. Do not mark this custom list as trusted. Keep necessary official filters for supported trusted scriptlets. Import on actual devices has not been tested.

The VPS systemd timer runs every Monday at 03:00 Asia/Ho_Chi_Minh. It downloads all configured sources, removes exact duplicates, rejects malformed or suspiciously incomplete inputs, and publishes only changed outputs. Failed builds leave the previous published filters in place.

Sources: [configuration](source/List_Filter_ADS.txt), [AdGuard Filters](https://github.com/AdguardTeam/AdguardFilters), [EasyList/EasyPrivacy](https://github.com/easylist/easylist), [ABPVN](https://github.com/abpvn/abpvn), [uAssets](https://github.com/uBlockOrigin/uAssets), and [local rules](source/myfilter.txt). Modified aggregate and worker: [GPL-3.0](LICENSE). Upstream copyright and license terms apply; see the Vietnamese README for details. No unauthorized premium lists are included.

Legacy Filer_Path and Lowji194_Filter_ADS.txt URLs have been retired. See [README.md](README.md) for operation and troubleshooting.
