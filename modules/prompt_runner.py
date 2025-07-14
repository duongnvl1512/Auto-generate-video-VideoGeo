import openpyxl
import time
from playwright.sync_api import Page

def delay(seconds):
    print(f"⏳ Chờ {seconds} giây...")
    time.sleep(seconds)

def read_prompts(path="data/prompts.xlsx"):
    wb = openpyxl.load_workbook(path)
    sheet = wb.active
    prompts = []

    for row in sheet.iter_rows(min_row=2, values_only=True):
        prompt_id, prompt_text = row[0], row[1]
        if prompt_id is None:
            break
        prompts.append({"id": int(prompt_id), "prompt": prompt_text})
    return prompts

def run_prompt_loop(page: Page):
    prompts = read_prompts()
    print(f"🔁 Tổng số prompt: {len(prompts)}")

    for item in prompts:
        prompt_id = item["id"]
        prompt_text = item["prompt"]

        print(f"\n📥 Bắt đầu vòng lặp ID = {prompt_id}: {prompt_text}")

        try:
            # Nhập prompt vào ô
            page.wait_for_selector("textarea", timeout=10000)
            page.fill("textarea", prompt_text)
            delay(2)

            # Click "Generate Script"
            page.click("#script-generate-script-button", timeout=10000)
            print("🚀 Đã click Generate Script")
            delay(20)

            # Click "Generate video"
            page.click("button:has-text('Generate video')", timeout=10000)
            print("🎬 Đã click Generate video")
            delay(45)

            # Quay về homepage
            page.click("a[href='/']", timeout=10000)
            print("🏠 Đã quay về trang chủ")
            delay(5)

            # Click "Create a video"
            page.click("text=Create a video", timeout=10000)
            print("🆕 Tạo video mới cho vòng lặp tiếp theo")
            delay(5)

        except Exception as e:
            print(f"❌ Lỗi tại ID = {prompt_id}: {e}")
            print("⏸ Tạm dừng 2 phút để xử lý thủ công...")
            delay(120)
