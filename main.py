from playwright.sync_api import sync_playwright
import requests
import time


PAGE_URL = "https://rabotavdodo.ru/Lukhovitsy/eec89bd2a31db46311eedc5e2260fa4f/4254ceb0edc5826d11eff2ad492b901d"

API_URL = "https://rabotavdodo.ru/api/dodois/vacancies?localities=eec89bd2a31db46311eedc5e2260fa4f&staffTypes=Courier"


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120 Safari/537.36"
            )
        )

        page = context.new_page()

        print("OPEN PAGE")

        page.goto(
            PAGE_URL,
            wait_until="domcontentloaded",
            timeout=60000
        )

        time.sleep(10)

        print("PAGE:", page.url)
        print("TITLE:", page.title())


        cookies = context.cookies()

        print("COOKIES:", len(cookies))


        session = requests.Session()

        for cookie in cookies:
            session.cookies.set(
                cookie["name"],
                cookie["value"],
                domain=cookie["domain"]
            )


        headers = {
            "User-Agent": page.evaluate("navigator.userAgent"),
            "Accept": "application/json,text/plain,*/*",
            "Referer": PAGE_URL
        }


        print("REQUEST API")


        response = session.get(
            API_URL,
            headers=headers,
            timeout=30
        )


        print("STATUS:", response.status_code)

        print("ANSWER:")
        print(response.text[:5000])


        browser.close()



if __name__ == "__main__":
    main()
