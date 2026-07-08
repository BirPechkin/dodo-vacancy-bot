import os
import subprocess
import time
from playwright.sync_api import sync_playwright

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

subprocess.run(
    ["python", "-m", "playwright", "install", "chromium"],
    check=True
)

url = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/146 Safari/537.36",
        locale="ru-RU"
    )

    page = context.new_page()

    response = page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("FIRST STATUS:", response.status)

    # ждём прохождение JS проверки
    time.sleep(10)

    print("URL:", page.url)

    cookies = context.cookies()
    print("COOKIES:", cookies)

    response = page.goto(
        url,
        wait_until="networkidle",
        timeout=60000
    )

    print("SECOND STATUS:", response.status)

    print(page.content()[:3000])

    browser.close()
