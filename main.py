from playwright.sync_api import sync_playwright
import requests
import os


CITY_ID = "eec89bd2a31db46311eedc5e2260fa4f"

API_URL = (
    "https://rabotavdodo.ru/api/dodois/vacancies"
    f"?localities={CITY_ID}&staffTypes=Courier"
)


def get_cookies():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            executable_path="/opt/render/project/src/.venv/lib/python3.14/site-packages/playwright/driver/package/.local-browsers/chromium-1228/chrome-linux64/chrome",
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page()

        page.goto(
            "https://rabotavdodo.ru/vacancies/courier",
            wait_until="networkidle",
            timeout=60000
        )

        cookies = page.context.cookies()

        browser.close()

        return cookies


def main():

    cookies = get_cookies()

    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(
            cookie["name"],
            cookie["value"]
        )

    response = session.get(
        API_URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("STATUS:", response.status_code)
    print("URL:", API_URL)
    print(response.text)


if __name__ == "__main__":
    main()
