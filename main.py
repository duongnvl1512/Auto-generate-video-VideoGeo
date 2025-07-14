from core.browser import create_browser
from core.navigator import open_target, click_login
from modules.login import login_with_email_and_wait_otp
from modules.workflow import click_create_video, click_continue_in_media_step, is_on_prompt_page
from modules.prompt_runner import run_prompt_loop

from playwright.sync_api import TimeoutError

def main():
    playwright, browser, context, page = create_browser()

    try:
        open_target(page)

        try:
            page.wait_for_selector("text=Log In", timeout=5000)
            print("🔐 Chưa login, thực hiện đăng nhập...")
            click_login(page)
            login_with_email_and_wait_otp(page)
        except TimeoutError:
            print("✅ Đã login sẵn. Bỏ qua bước đăng nhập.")

        click_create_video(page)
        click_continue_in_media_step(page)

        if is_on_prompt_page(page):
            print("🎯 Giao diện prompt đã sẵn sàng.")
            run_prompt_loop(page)
        else:
            print("❌ Không tìm thấy giao diện prompt. Dừng.")

        input("🟢 Hoàn tất. Nhấn Enter để thoát...")

    finally:
        browser.close()
        playwright.stop()

if __name__ == "__main__":
    main()
