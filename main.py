from playwright.sync_api import sync_playwright
from playwright.__main__ import main as playwright_main
import requests
import os

# Скачать браузер, если его нет
os.system("playwright install chromium")

URL = "https://rabotavdodo.ru/api/dodois/vacancies?localities=eec89bd2a31db46311eedc5e2260fa4f&staffTypes=Courier"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    response = page.goto(URL, wait_until="networkidle")
    print("FIRST STATUS:", response.status)

    cookies = page.context.cookies()
    browser.close()

session = requests.Session()

for cookie in cookies:
    session.cookies.set(cookie["name"], cookie["value"])

r = session.get(URL, headers={
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://rabotavdodo.ru/"
})

print("SECOND STATUS:", r.status_code)
print(r.text)
