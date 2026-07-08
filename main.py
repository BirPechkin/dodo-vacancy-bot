from playwright.sync_api import sync_playwright
import requests


CITY_KEY = "eec89bd2a31db46311eedc5e2260fa4f"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
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


session = requests.Session()

for cookie in cookies:
    session.cookies.set(
        cookie["name"],
        cookie["value"]
    )


url = (
    "https://rabotavdodo.ru/api/dodois/vacancies"
    f"?localities={CITY_KEY}"
    "&staffTypes=Courier"
)


response = session.get(
    url,
    headers={
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://rabotavdodo.ru/vacancies/courier"
    }
)


print("STATUS:", response.status_code)
print(response.text)
