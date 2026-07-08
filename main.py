from playwright.sync_api import sync_playwright
import requests
import time

URL = "https://rabotavdodo.ru/Lukhovitsy/eec89bd2a31db46311eedc5e2260fa4f/4254ceb0edc5826d11eff2ad492b901d?tabSlug=all#calculator"

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=True
    )

    page = browser.new_page()

    page.goto(URL, wait_until="networkidle", timeout=60000)

    time.sleep(5)

    html = page.content()

    print("PAGE LOADED")
    print(html[:1000])

    browser.close()
