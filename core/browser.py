from playwright.sync_api import sync_playwright
from config.settings import HEADLESS
import os

# Dùng thư mục này để lưu "hồ sơ trình duyệt"
USER_DATA_DIR = os.path.abspath("browser_profile")

def create_browser():
    playwright = sync_playwright().start()

    # Sử dụng persistent context thay vì new_context
    browser = playwright.chromium.launch_persistent_context(
        USER_DATA_DIR,
        headless=HEADLESS,
        args=["--start-maximized"]
    )

    # Lấy trang hiện tại (tab đầu tiên)
    page = browser.pages[0] if browser.pages else browser.new_page()

    return playwright, browser, browser, page
