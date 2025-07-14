from playwright.sync_api import Page
from config import settings
import time

def delay(seconds=settings.DELAY):
    time.sleep(seconds)

def click_create_video(page: Page):
    print("🎬 Click 'Create a video'...")

    try:
        page.click("text=Create a video", timeout=10000)
        delay()
    except Exception:
        print("⚠️ Không click được 'Create a video'. Tạm dừng 2 phút...")
        delay(120)

def click_continue_in_media_step(page: Page):
    print("👉 Click 'Continue' tại bước chọn media...")

    try:
        page.click("button:has-text('Continue')", timeout=10000)
        delay()
    except Exception:
        print("⚠️ Không thấy nút 'Continue'. Tạm dừng 2 phút...")
        delay(120)


def is_on_prompt_page(page: Page):
    try:
        page.wait_for_selector("text=What is your video about?", timeout=10000)
        print("✅ Đã chuyển đến bước nhập Prompt.")
        return True
    except:
        print("❌ Không tìm thấy giao diện Prompt.")
        return False
