from playwright.sync_api import sync_playwright
import requests

URL = "https://rabotavdodo.ru/api/dodois/vacancies?localities=eec89bd2a31db46311eedc5e2260fa4f&staffTypes=Courier"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Заходим на API через браузер, чтобы пройти защиту
    response = page.goto(URL, wait_until="networkidle")

    print("FIRST STATUS:", response.status)

    cookies = page.context.cookies()
    browser.close()

session = requests.Session()

for cookie in cookies:
    session.cookies.set(cookie["name"], cookie["value"])

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://rabotavdodo.ru/"
}

r = session.get(URL, headers=headers)

print("SECOND STATUS:", r.status_code)
print("ANSWER:")
print(r.text)
