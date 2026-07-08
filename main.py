from playwright.sync_api import sync_playwright
import os
import time


URL = "https://rabotavdodo.ru/Lukhovitsy/eec89bd2a31db46311eedc5e2260fa4f/4254ceb0edc5826d11eff2ad492b901d?tabSlug=all#calculator"


def main():
    # путь, куда Render ставит браузер при PLAYWRIGHT_BROWSERS_PATH=0
    browser_path = "/opt/render/project/src/.venv/lib/python3.14/site-packages/playwright/driver/package/.local-browsers/chromium-1228/chrome-linux64/chrome"

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            executable_path=browser_path,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page()

        page.goto(
            URL,
            wait_until="networkidle",
            timeout=60000
        )

        time.sleep(5)

        print("STATUS:", page.title())
        print("URL:", page.url)

        print(page.locator("body").inner_text()[:3000])

        browser.close()


if __name__ == "__main__":
    main()
