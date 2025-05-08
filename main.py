import os
import time
import schedule
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Load mã sinh viên và mật khẩu từ file .env
load_dotenv()
ma_sv = os.getenv("STUDENT_ID")
mat_khau = os.getenv("PASSWORD")

def khoi_dong_trinh_duyet():
    # Tạo thư mục lichhoc để lưu file
    thu_muc_luu = "lichhoc"
    if not os.path.exists(thu_muc_luu):
        os.makedirs(thu_muc_luu)
    
    # Đường dẫn đến chromedriver
    duong_dan_chromedriver = r"C:\Study\PY-TĐHQT\Luong-baitaplon\chromedriver.exe"
    if not os.path.exists(duong_dan_chromedriver):
        print("Không tìm thấy chromedriver! Kiểm tra file chromedriver.exe trong thư mục dự án.")
        return None
    
    # Khởi động Chrome
    dich_vu = Service(duong_dan_chromedriver)
    trinh_duyet = webdriver.Chrome(service=dich_vu)
    return trinh_duyet

def dang_nhap(trinh_duyet):
    # Vào trang đăng nhập
    trinh_duyet.get("https://sinhvien.dau.edu.vn/sinh-vien-dang-nhap.html")
    
    # Chờ trang tải và tìm các ô nhập
    time.sleep(3)  # Chờ đơn giản thay vì WebDriverWait
    o_nhap_ma_sv = trinh_duyet.find_element(By.ID, "UserName")
    o_nhap_mat_khau = trinh_duyet.find_element(By.ID, "Password")
    
    # Kiểm tra thông tin đăng nhập
    if not ma_sv or not mat_khau:
        print("Thiếu mã sinh viên hoặc mật khẩu! Kiểm tra file .env.")
        return False
    
    # Nhập thông tin
    o_nhap_ma_sv.send_keys(ma_sv)
    o_nhap_mat_khau.send_keys(mat_khau)
    
    # Nhập mã CAPTCHA
    print("Xem mã CAPTCHA trên website.")
    ma_captcha = input("Nhập mã CAPTCHA: ")
    o_nhap_captcha = trinh_duyet.find_element(By.ID, "Captcha")
    o_nhap_captcha.send_keys(ma_captcha)
    
    # Bấm nút đăng nhập
    nut_dang_nhap = trinh_duyet.find_element(By.CSS_SELECTOR, "input[type='submit']")
    nut_dang_nhap.click()
    
    # Chờ xem có đăng nhập thành công không
    time.sleep(3)
    if "dashboard.html" in trinh_duyet.current_url:
        print("Đăng nhập thành công!")
        return True
    else:
        print("Đăng nhập thất bại! Kiểm tra mã sinh viên, mật khẩu, hoặc CAPTCHA.")
        return False

def lay_lich_hoc(trinh_duyet):
    ngay_hien_tai = datetime.now().strftime("%Y-%m-%d")
    ngay_hien_tai_vn = datetime.now().strftime("%d/%m/%Y")
    lich_hoc = f"Lịch học ngày {ngay_hien_tai_vn}:\n"
    
    # Vào trang lịch học
    print("Đang tải lịch học...")
    trinh_duyet.get("https://sinhvien.dau.edu.vn/lich-theo-tuan.html")
    time.sleep(3)  # Chờ trang tải
    
    # Lấy dữ liệu từ bảng
    soup = BeautifulSoup(trinh_duyet.page_source, "html.parser")
    bang_lich = soup.find("table", class_="table")
    
    if bang_lich:
        cac_dong = bang_lich.find_all("tr")
        co_lich = False
        for dong in cac_dong[1:]:
            cac_cot = dong.find_all("td")
            if len(cac_cot) >= 5:
                ngay = cac_cot[0].text.strip()
                if ngay == ngay_hien_tai_vn:
                    mon_hoc = cac_cot[1].text.strip()
                    gio_hoc = cac_cot[2].text.strip()
                    phong_hoc = cac_cot[3].text.strip()
                    lich_hoc += f"- Môn: {mon_hoc}, Thời gian: {gio_hoc}, Phòng: {phong_hoc}\n"
                    co_lich = True
        if not co_lich:
            lich_hoc += "Không có lịch học hôm nay.\n"
    else:
        lich_hoc += "Không tìm thấy lịch học!\n"
    
    # Lưu file text
    ten_file_text = os.path.join("lichhoc", f"lich_hoc_{ngay_hien_tai}.txt")
    with open(ten_file_text, "w", encoding="utf-8") as f:
        f.write(lich_hoc)
    print(f"Đã lưu file text: {ten_file_text}")
    
    return lich_hoc

def chay():
    print("Bắt đầu lấy lịch học...")
    trinh_duyet = khoi_dong_trinh_duyet()
    if not trinh_duyet:
        return
    if dang_nhap(trinh_duyet):
        lich_hoc = lay_lich_hoc(trinh_duyet)
        print(lich_hoc)
    else:
        print("Không lấy được lịch học vì đăng nhập thất bại.")
    trinh_duyet.quit()
    print("Hoàn tất!")

# Lên lịch chạy
schedule.every().day.at("06:00").do(chay)
schedule.every().day.at("12:00").do(chay)

if __name__ == "__main__":
    print("Chương trình lấy lịch học tự động")
    chay()
    print("Chương trình sẽ chạy lúc 6h sáng và 12h trưa mỗi ngày.")
    while True:
        schedule.run_pending()
        time.sleep(60)