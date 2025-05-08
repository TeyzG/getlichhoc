# Tự Động Lấy Lịch Học từ Hệ Thống Đại học Kiến Trúc Đà Nẵng

Chương trình Python này tự động đăng nhập vào hệ thống quản lý sinh viên của trường Đại học Kiến Trúc Đà Nẵng, lấy lịch học theo ngày và lưu vào file text. Chương trình có thể chạy theo lịch trình cố định (6h sáng và 12h trưa mỗi ngày).


## Cài Đặt

1. **Yêu Cầu Hệ Thống**:
   - Python 3.x
   - Thư viện: `selenium`, `beautifulsoup4`, `python-dotenv`, `schedule`
   - ChromeDriver (đặt tại đường dẫn được chỉ định trong code hoặc cập nhật đường dẫn trong file).

2. **. Cấu Hình:**
Tạo file .env trong thư mục dự án với nội dung:
![image](https://github.com/user-attachments/assets/3aa3ea89-a4e3-4571-9f30-b6c11a835025)

Đảm bảo ChromeDriver được đặt đúng đường dẫn

![image](https://github.com/user-attachments/assets/f0638eb8-2040-41af-ab2e-856bf0b1497a)
Chạy Tự Động: Chương trình sẽ tự động chạy vào 6h sáng và 12h trưa mỗi ngày sau khi khởi động.
![image](https://github.com/user-attachments/assets/60862cbe-28c3-4044-ae76-86c68d345841)

Thư Mục và File
Thư mục lichhoc: Chứa các file lịch học được lưu tự động, định dạng lich_hoc_YYYY-MM-DD.txt.
File .env: Lưu trữ thông tin đăng nhập (bắt buộc).
![image](https://github.com/user-attachments/assets/eeb4165d-0235-40e9-8d6d-c25bad2e6f46)

**Ghi Chú**
CAPTCHA: Chương trình yêu cầu nhập mã CAPTCHA thủ công tại Terminal khi đăng nhập.
![image](https://github.com/user-attachments/assets/cbe661af-7587-4d33-8e79-4a98856e81ab)![image](https://github.com/user-attachments/assets/08e61f12-d669-4304-8b5b-503f5d1ab018)

Kiểm Tra Lỗi: Chương trình sẽ thông báo nếu không tìm thấy ChromeDriver hoặc thiếu thông tin đăng nhập.

Tác Giả
Tên: Nguyễn Hoàng Lương
Email: Luong_2251220018@dau.edu.vn
MSSV: 2251220018
