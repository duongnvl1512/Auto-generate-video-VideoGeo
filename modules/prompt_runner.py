import openpyxl
import time
from playwright.sync_api import Page

def delay(seconds):
    print(f"⏳ Chờ {seconds} giây...")
    time.sleep(seconds)

def read_prompts(path="data/prompts.xlsx"):
    print(f"📄 Đang đọc dữ liệu prompt từ: {path}")
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    prompts = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        prompt_id, prompt_text = row[0], row[1]
        if prompt_id is None:
            break
        prompts.append({"id": int(prompt_id), "prompt": prompt_text})

    print(f"✅ Đọc thành công {len(prompts)} prompt.")
    return prompts

def wait_for_prompt_input(page: Page, timeout=30000):
    print("⏳ Đợi chuyển sang giao diện nhập prompt...")

    try:
        page.wait_for_selector("text=What is your video about?", timeout=timeout)
        page.wait_for_selector("textarea:not([aria-hidden='true'])", timeout=timeout)
        print("✅ Đã sẵn sàng nhập prompt.")
    except Exception as e:
        print("⚠️ Không vào được giao diện prompt sau khi tạo video.")
        print("🌐 URL:", page.url)
        print("📄 Title:", page.title())
        raise e

def run_prompt_loop(page: Page):
    prompts = read_prompts()
    print(f"🔁 Tổng số prompt: {len(prompts)}")

    for item in prompts:
        prompt_id = item["id"]
        prompt_text = item["prompt"]

        print(f"\n📥 Bắt đầu vòng lặp ID = {prompt_id}:")
        print(f"📄 Prompt: {prompt_text[:80]}...")

        try:
            wait_for_prompt_input(page)

            print("📝 Điền nội dung vào textarea...")
            page.fill("textarea:not([aria-hidden='true'])", prompt_text)
            delay(2)

            print("🚀 Click 'Generate Script'...")
            page.click("#script-generate-script-button", timeout=10000)
            delay(20)

            print("🎬 Click 'Generate video'...")
            page.click("button:has-text('Generate video')", timeout=10000)
            delay(45)

            print("🏠 Quay về trang chủ...")
            page.click("a[href='/']", timeout=10000)
            delay(5)

            print("🎬 Click lại 'Create a video'...")
            page.click("text=Create a video", timeout=10000)
            delay(5)

            print("👉 Click 'Continue' để vào giao diện Prompt tiếp theo...")
            page.click("text=Continue", timeout=10000)
            delay(5)

        except Exception as e:
            print(f"❌ Lỗi tại ID = {prompt_id}: {e}")
            print("⏸ Tạm dừng 2 phút để người dùng xử lý thủ công...")
            delay(120)
