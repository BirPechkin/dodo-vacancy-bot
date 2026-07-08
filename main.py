import os
import subprocess
from playwright.sync_api import sync_playwright

# Хранилище браузера внутри проекта
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

# Установка Chromium перед запуском
subprocess.run(
    ["python", "-m", "playwright", "install", "chromium"],
    check=True
)

url = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/146 Safari/537.36",
        locale="ru-RU"
    )

    response = page.goto(
        url,
        wait_until="networkidle",
        timeout=60000
    )

    print("STATUS:", response.status)

    text = page.content()

    print(text[:3000])

    browser.close()
