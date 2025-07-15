from playwright.sync_api import Page
from config import settings
import time

def delay(seconds=settings.DELAY):
    print(f"⏳ Chờ {seconds} giây...")
    time.sleep(seconds)

def click_create_video(page: Page):
    print("🎬 Bắt đầu click 'Create a video'...")
    print("🌐 URL hiện tại:", page.url)
    print("📄 Title hiện tại:", page.title())

    try:
        page.click("text=Create a video", timeout=10000)
        delay()
        print("✅ Đã click 'Create a video'")
        print("🌐 URL sau khi click:", page.url)
    except Exception:
        print("⚠️ Không click được 'Create a video'. Tạm dừng 2 phút...")
        delay(120)

def click_continue_in_media_step(page: Page):
    print("👉 Đang click 'Continue' tại bước chọn media...")

    try:
        page.click("button:has-text('Continue')", timeout=10000)
        delay()
        print("✅ Đã click 'Continue' và chờ giao diện mới")
    except Exception:
        print("⚠️ Không thấy nút 'Continue'. Tạm dừng 2 phút...")
        delay(120)

def is_on_prompt_page(page: Page):
    print("🔍 Kiểm tra xem đã vào giao diện prompt chưa...")

    try:
        page.wait_for_selector("text=What is your video about?", timeout=10000)
        print("✅ Đã chuyển đến bước nhập Prompt.")
        print("🌐 URL hiện tại:", page.url)
        return True
    except:
        print("❌ Không tìm thấy giao diện Prompt.")
        return False
