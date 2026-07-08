from playwright.sync_api import sync_playwright
import time


URL = "https://rabotavdodo.ru/Lukhovitsy/eec89bd2a31db46311eedc5e2260fa4f/4254ceb0edc5826d11eff2ad492b901d?tabSlug=all#calculator"


def main():
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
            URL,
            wait_until="networkidle",
            timeout=60000
        )

        time.sleep(5)

        print("TITLE:")
        print(page.title())

        print("URL:")
        print(page.url)

        text = page.locator("body").inner_text()

        print("PAGE TEXT:")
        print(text[:3000])

        browser.close()


if __name__ == "__main__":
    main()
