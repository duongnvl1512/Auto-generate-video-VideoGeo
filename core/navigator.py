import time
from config import settings
from playwright.sync_api import Page

def delay():
    time.sleep(settings.DELAY)

def open_target(page: Page):
    print(f"🔗 Truy cập {settings.TARGET_URL}")
    page.goto(settings.TARGET_URL)
    delay()

def click_login(page: Page):
    print("👉 Click 'Log In'...")

    try:
        page.click("text=Log In", timeout=20000)
        delay()
        print("✅ Đã click Log In.")
    except Exception as e:
        print("⚠️ Không tìm thấy nút Log In. Có thể gặp checkpoint.")
        print("⏸ Tạm dừng 2 phút để người dùng thao tác thủ công...")
        delay(120)

