import openpyxl
import time
from playwright.sync_api import Page
from config import settings

def delay(seconds=settings.DELAY):
    time.sleep(seconds)

def read_first_account(path: str = "data/accounts.xlsx"):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        email, password = row
        if email and password:
            return {"email": email, "password": password}
    return None

def login_with_email_and_wait_otp(page: Page):
    account = read_first_account()
    if not account:
        print("❌ Không tìm thấy tài khoản trong Excel.")
        return

    email = account["email"]
    print(f"📨 Điền email: {email}")

    try:
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

    account = read_first_account()
    if not account:
        print("❌ Không tìm thấy tài khoản trong Excel.")
        return

    email = account["email"]
    print(f"📨 Điền email: {email}")

    page.wait_for_selector("input[type='email']", timeout=10000)
    page.fill("input[type='email']", email)
    delay()

    print("👉 Click 'Continue with email'...")
    page.click("button:has-text('Continue with email')")
    delay()

    # Chờ người dùng nhập mã xác thực và bấm “Sign In”
    print("⏸ Chờ người dùng nhập mã OTP và bấm 'Sign In' (60s)...")
    delay(60)
