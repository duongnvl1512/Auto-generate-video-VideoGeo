import openpyxl
import time
from playwright.sync_api import Page
from config import settings

def delay(seconds=settings.DELAY):
    print(f"⏳ Chờ {seconds} giây...")
    time.sleep(seconds)

def read_first_account(path: str = "data/accounts.xlsx"):
    print(f"📄 Đang đọc tài khoản từ file: {path}")
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        email, password = row
        if email and password:
            print(f"✅ Đã đọc tài khoản: {email}")
            return {"email": email, "password": password}
    print("❌ Không tìm thấy tài khoản hợp lệ trong file.")
    return None

def login_with_email_and_wait_otp(page: Page):
    account = read_first_account()
    if not account:
        return

    email = account["email"]
    print(f"📨 Điền email: {email}")

    try:
        print("⌛ Đợi input email xuất hiện...")
        page.wait_for_selector("input[type='email']", timeout=10000)
        page.fill("input[type='email']", email)
        delay()

        print("👉 Click 'Continue with email'...")
        page.click("button:has-text('Continue with email')", timeout=10000)
        delay()

    except Exception as e:
        print("⚠️ Không thể điền email hoặc click 'Continue'.")
        print("⏸ Tạm dừng 2 phút để người dùng thao tác thủ công...")
        delay(120)

    print("⏸ Chờ người dùng nhập mã OTP và bấm 'Sign In' (60s)...")
    delay(60)
