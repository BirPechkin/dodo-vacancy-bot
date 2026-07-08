import os
import subprocess
import time
from playwright.sync_api import sync_playwright

os.environ["PLAYWRIGHT_BROWSERS_PATH"] = "0"

# Для первого запуска скачиваем Chromium
subprocess.run(
    ["python", "-m", "playwright", "install", "chromium"],
    check=True
)

url = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier&locale=ru"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True
    )

    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/146 Safari/537.36",
        locale="ru-RU"
    )

    page = context.new_page()

    # Первый заход — пройти защиту ServicePipe
    response = page.goto(
        url,
        wait_until="domcontentloaded",
        timeout=60000
    )

    print("FIRST STATUS:", response.status)

    # ждём выдачу cookies
    time.sleep(10)

    print("COOKIES:")
    print(context.cookies())

    # Второй запрос после прохождения защиты
    response = page.goto(
        url,
        wait_until="networkidle",
        timeout=60000
    )

    print("SECOND STATUS:", response.status)

    print("ANSWER:")
    print(page.text_content("body"))

    browser.close()
