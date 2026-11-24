# AdsBlock Filter — Lowji194

[English](README-EN.md) · [Website](https://theloi.io.vn/)

Bộ lọc quảng cáo và theo dõi tổng hợp từ các nguồn công khai, dành riêng cho AdGuard Browser Extension (máy tính) và AdGuard Android (ứng dụng đầy đủ).

## Đăng ký bộ lọc

| Thiết bị | Link đăng ký |
|---|---|
| Desktop | [AdGuard_Desktop.txt](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt) |
| Android | [AdGuard_Android.txt](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt) |

**Chỉ thêm một bộ lọc tương ứng với thiết bị.** Không nhập hai file cùng lúc.

### Desktop

Cài [AdGuard Browser Extension](https://adguard.com/en/adguard-browser-extension/overview.html), mở Settings → Filters → Custom → Add custom filter, dán URL Desktop rồi lưu và bật bộ lọc.

### Android

Cài [AdGuard for Android](https://adguard.com/en/adguard-android/overview.html), mở Protection → Ad blocking → Filters → Custom filters → Add custom filter, dán URL Android. Tên mục có thể khác theo phiên bản ứng dụng. Dùng bộ lọc nội dung, không nhập vào DNS filters hay Android Private DNS. Để lọc HTTPS cần bật tính năng tương ứng theo hướng dẫn AdGuard; không phải mọi ứng dụng đều hỗ trợ lọc HTTPS.

### Lưu ý

- Đây là bộ lọc tùy chỉnh tổng hợp, không phải bộ lọc chính thức của AdGuard. Không cần bật thêm nhiều bộ lọc trùng nội dung; nên giữ các bộ lọc chính thức cần thiết cho scriptlet đáng tin cậy và các tính năng không có trong bản tổng hợp.
- Chrome/Edge Manifest V3 có giới hạn rule; một phần rule có thể không được áp dụng. Nếu gặp cảnh báo giới hạn, dùng các bộ lọc chính thức tối ưu hoặc Firefox. Chưa kiểm thử nhập trực tiếp trên thiết bị.
- Không bật chế độ trusted chỉ để cài bộ lọc này. Worker loại bỏ scriptlet yêu cầu quyền trusted và cú pháp uBlock riêng không tương thích.
- Không bảo đảm chặn mọi quảng cáo, nhất là YouTube/quảng cáo tích hợp trong nội dung ứng dụng. Nếu website/app lỗi, thử tắt bộ lọc hoặc tạo ngoại lệ.
- Không dùng các file này cho AdGuard Home.

## Nguồn và giấy phép

Danh sách cập nhật: [source/List_Filter_ADS.txt](source/List_Filter_ADS.txt). Các nguồn hiện tại:

- [AdGuard Filters](https://github.com/AdguardTeam/AdguardFilters) — GPL-3.0; Base (bao gồm EasyList) và Mobile Ads (Android).
- [EasyList / EasyPrivacy](https://github.com/easylist/easylist) — giấy phép theo upstream (GPL-3.0 hoặc CC BY-SA theo điều khoản của dự án); dùng bản EasyPrivacy tối ưu do AdGuard phân phối.
- [ABPVN](https://github.com/abpvn/abpvn) — GPL-3.0; bản AdGuard, ưu tiên website Việt Nam.
- [uBlock Origin uAssets](https://github.com/uBlockOrigin/uAssets) — GPL-3.0; bản Badware risks tối ưu cho AdGuard.
- [Quy tắc bổ sung](source/myfilter.txt) — Lowji194.

Bản tổng hợp đã được sửa đổi: chuẩn hóa hosts/domain, loại trùng chính xác, loại cú pháp không phù hợp và phân loại theo nền tảng. Bản tổng hợp và worker được phân phối theo [GPL-3.0](LICENSE), giữ bản quyền của các tác giả upstream. URL nguồn được ghi trong header của từng file. Không tổng hợp nguồn VIP/premium chưa có quyền phân phối lại, danh sách DNS tổng hợp, raw uBlock hoặc URLhaus dạng không phù hợp. Badware risks chỉ bổ sung, không thay thế bảo vệ malware chuyên dụng.

## Cập nhật tự động

Worker chạy trên VPS bằng systemd mỗi thứ Hai lúc 03:00 (UTC+7). Tải song song nguồn công khai, retry 3 lần, kiểm tra định dạng/số lượng, lọc trùng và chỉ commit khi nội dung thay đổi. Nếu một nguồn bị lỗi hoặc số lượng rule giảm bất thường, không xuất bản bản mới. Git push sử dụng xác thực GitHub CLI đã cấu hình trên VPS, không lưu token trong repository.

Cấu trúc:

- source/List_Filter_ADS.txt — danh sách nguồn theo [common], [desktop], [android].
- source/myfilter.txt — quy tắc bổ sung thủ công.
- filters/ — hai file kết quả.
- worker/ — trình tổng hợp và xuất bản.
- systemd/ — service và timer mẫu.

Trên VPS hiện tại, unit được cài trong /usr/local/lib/systemd/system/ và timer được nối trực tiếp vào timers.target qua thư mục timers.target.wants (do /etc chỉ đọc). systemctl có thể hiển thị UnitFileState=disabled dù timer đang active và đã có dependency khởi động. Không cần cron.

Chạy cập nhật thủ công trên VPS đã triển khai:

    systemctl start adsblock-filter.service
    systemctl list-timers adsblock-filter.timer
    journalctl -u adsblock-filter.service -n 50 --no-pager

Các URL cũ trong Filer_Path và Lowji194_Filter_ADS.txt đã ngừng sử dụng; hãy chuyển sang URL mới ở trên.

## Liên hệ

[GitHub](https://github.com/lowji194) · [Website](https://theloi.io.vn/)
