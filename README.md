[![🇺🇸 English](https://img.shields.io/badge/Language-English-blue?style=for-the-badge&logo=Google%20Translate)](README-EN.md)
---
# **🔥Bộ Lọc Quảng Cáo By Lợi Nguyễn🔥**

Đây là bộ lọc quảng cáo nâng cao được phát triển bởi **Nguyễn Thế Lợi**. Bộ lọc tổng hợp các nguồn công khai, được tối ưu riêng cho **AdGuard Browser Extension (Desktop)** và **AdGuard for Android**, giúp chặn quảng cáo, hạn chế theo dõi và cải thiện trải nghiệm duyệt web.

---

## 📅 **Thông Tin Cập Nhật**

- **Website**: [Lowji194](https://theloi.io.vn/)
- **Dành cho**: AdGuard Browser Extension / AdGuard for Android
- **Tác giả**: Nguyễn Thế Lợi
- **Mô tả**: Bộ lọc chặn quảng cáo và bảo vệ quyền riêng tư
- **Cập nhật**: Tự động mỗi 7 ngày, lúc 03:00 sáng thứ Hai (UTC+7)
- **Mã nguồn**: [GitHub](https://github.com/lowji194/AdsBlock-Filter)
- **SĐT**: 0963 159 294
- **Facebook**: [Nguyễn Thế Lợi](https://www.facebook.com/Lowji194/)

---

## 🚀 **Hướng Dẫn Sử Dụng**

Bộ lọc được chia thành hai phiên bản riêng biệt dành cho máy tính và Android. Bạn chỉ cần cài AdGuard và đăng ký một URL phù hợp với thiết bị của mình.

### 1. **Cài Đặt AdGuard**

- 🖥️ **AdGuard Browser Extension (Desktop)**: Cài đặt từ [Chrome Web Store](https://chromewebstore.google.com/detail/adguard-adblocker/bgnkhhnnamicmpeenaelnjfhikgbkllg), [Firefox Add-ons](https://addons.mozilla.org/firefox/addon/adguard-adblocker/) hoặc [trang tải chính thức](https://adguard.com/en/adguard-browser-extension/overview.html).
- 📱 **AdGuard for Android**: Tải ứng dụng đầy đủ từ [trang chủ AdGuard](https://adguard.com/en/adguard-android/overview.html).

### 2. **Thêm Bộ Lọc vào AdGuard**

#### 🖥️ AdGuard Browser Extension — Desktop

1. Nhấp vào biểu tượng **AdGuard** trên trình duyệt.
2. Chọn **Cài đặt (Settings)** → **Bộ lọc (Filters)**.
3. Mở mục **Tùy chỉnh (Custom)**, chọn **Thêm bộ lọc (Add custom filter)** và nhập URL sau:

```text
https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt
```

[![Desktop](https://img.shields.io/badge/AdGuard-Desktop-4285F4?style=for-the-badge&logo=adguard&logoColor=white)](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Desktop.txt)

#### 📱 AdGuard for Android — Mobile

1. Mở ứng dụng **AdGuard** và vào **Bảo vệ (Protection)**.
2. Chọn **Chặn quảng cáo (Ad blocking)** → **Bộ lọc (Filters)** → **Bộ lọc tùy chỉnh (Custom filters)**.
3. Chọn **Thêm bộ lọc** và nhập URL sau:

```text
https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt
```

[![Android](https://img.shields.io/badge/AdGuard-Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)](https://raw.githubusercontent.com/lowji194/AdsBlock-Filter/main/filters/AdGuard_Android.txt)

### 3. **Kích Hoạt Bộ Lọc**

**Desktop (Chrome / Edge / Firefox):** Bộ lọc Lowji194 Desktop là bộ lọc bổ sung nhẹ. Hãy bật **AdGuard Base filter**, **AdGuard Tracking Protection filter** (hoặc EasyPrivacy), **AdGuard Quick Fixes filter** nếu có và bộ lọc bảo mật **uBlock Origin – Badware risks** (nếu có) trong danh sách tích hợp sẵn của extension. Không nhập lại các bộ lọc lớn bằng URL tùy chỉnh. Nếu ABPVN tích hợp đã bật, có thể tắt bản tích hợp để tránh trùng với ABPVN trong Lowji194 Desktop.

**Android:** Bộ lọc tổng hợp đầy đủ như trước, không áp dụng ngân sách rule Desktop.

Sau khi thêm URL, hãy bật bộ lọc và kiểm tra trạng thái bảo vệ trong AdGuard. Bạn có thể cập nhật, bật hoặc tắt bộ lọc bất kỳ lúc nào trong phần cài đặt.

> **Lưu ý:** Chỉ thêm bộ lọc tương ứng với thiết bị, không nhập cả hai URL. Trên Android, sử dụng bộ lọc nội dung thay vì DNS filter; khả năng lọc HTTPS phụ thuộc ứng dụng và thiết lập thiết bị. Không đánh dấu bộ lọc là trusted. Chrome/Edge Manifest V3 có giới hạn quy tắc động và regex dùng chung. Worker giới hạn Desktop ở tối đa 3.000 dòng quy tắc thô để chừa ngân sách; số rule DNR thực tế sau chuyển đổi có thể khác. Xem [tài liệu MV3 của AdGuard](https://adguard.com/kb/adguard-browser-extension/mv3-version/). Nếu sử dụng URL cũ, hãy chuyển sang URL mới ở trên.

---

## ⚙️ **Thông Tin Kỹ Thuật**

Bộ lọc được tạo ra để giúp chặn quảng cáo, pop-up, các trình theo dõi và một số nội dung không mong muốn. Hệ thống worker tự động tổng hợp nguồn, chuẩn hóa quy tắc, loại bỏ trùng lặp và phân loại theo từng nền tảng.

### **Nguồn Bộ Lọc**

| Nguồn | Desktop | Android |
|---|:---:|:---:|
| [AdGuard Base / EasyList](https://github.com/AdguardTeam/AdguardFilters) | Tích hợp sẵn | ✅ |
| [EasyPrivacy](https://github.com/easylist/easylist) | Tích hợp sẵn | ✅ |
| [ABPVN List](https://github.com/abpvn/abpvn) | ✅ | ✅ |
| [uBlock Badware risks (bản tối ưu cho AdGuard)](https://github.com/uBlockOrigin/uAssets) | Tích hợp sẵn | ✅ |
| [Bộ lọc bổ sung của Lowji194](source/myfilter.txt) | ✅ | ✅ |
| [AdGuard Mobile Ads](https://github.com/AdguardTeam/AdguardFilters) | — | ✅ |

Các mục "Tích hợp sẵn" là khuyến nghị bật trực tiếp trong extension, không nằm trong file Desktop.

Danh sách nguồn: [List_Filter_ADS.txt](source/List_Filter_ADS.txt). Sử dụng các biến thể phù hợp với AdGuard; không tổng hợp nguồn VIP/premium chưa được phép phân phối lại, danh sách DNS tổng hợp hoặc URLhaus định dạng cũ.

### **Cơ Chế Cập Nhật Tự Động**

- **Chu kỳ:** 7 ngày/lần (03:00 sáng thứ Hai, UTC+7).
- **Hệ thống:** Python Worker + Systemd Timer trên VPS.
- **Ngân sách Desktop:** Tối đa 3.000 quy tắc thô, ưu tiên ABPVN và quy tắc cá nhân. Nếu vượt ngưỡng, dừng xuất bản thay vì cắt tùy tiện các rule hoặc ngoại lệ. Không giới hạn Android theo chính sách này.
- **Quy trình:** Tải nguồn → kiểm tra dữ liệu → lọc trùng → tạo hai bộ lọc → cập nhật GitHub nếu nội dung thay đổi.
- **An toàn:** Tự thử lại tối đa 3 lần; nếu nguồn lỗi hoặc số quy tắc giảm bất thường, giữ nguyên bản đã xuất bản.
- **Mã nguồn:** [Worker](worker/) · [Systemd](systemd/).

Trên VPS hiện tại, systemd unit được đặt tại /usr/local/lib/systemd/system/ và liên kết với timers.target do /etc chỉ đọc. Timer đang hoạt động, nhưng chưa kiểm thử khởi động lại VPS. Lệnh cập nhật thủ công:

```bash
systemctl start adsblock-filter.service
systemctl list-timers adsblock-filter.timer
journalctl -u adsblock-filter.service -n 50 --no-pager
```

### **Giấy Phép và Tương Thích**

Bản tổng hợp đã được sửa đổi và worker được phân phối theo [GPL-3.0](LICENSE). Bản quyền thuộc các tác giả nguồn tương ứng; điều khoản giấy phép upstream vẫn áp dụng (EasyList/EasyPrivacy có lựa chọn giấy phép theo dự án). Nguồn được ghi trong header của mỗi file.

Đây là dự án độc lập, không phải bộ lọc chính thức của AdGuard. Không dùng cho AdGuard Home hoặc Android Private DNS. Worker đã được kiểm thử và URL đã được xác minh; chưa kiểm thử nhập trực tiếp trên thiết bị. Không bảo đảm chặn mọi quảng cáo hoặc thay thế phần mềm chống mã độc.

---

## 📫 Liên hệ với tôi

- 📞 **SĐT:** 0963 159 294
- 🌐 **Website:** [lowji194.github.io](https://lowji194.github.io)
- 📌 **Facebook:** [Lowji194](https://facebook.com/Lowji194)

---

## ☕ Nếu bạn thấy dự án này hữu ích, một ly cà phê từ bạn sẽ là động lực tuyệt vời để mình tiếp tục phát triển thêm!

<p align="center">
  <img src="https://theloi.io.vn/pay/QR.png?text=QR+Code" alt="Mời cà phê" width="240" />
</p>
