from playwright.sync_api import sync_playwright
import requests
import time


URL = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier"


def main():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage"
            ]
        )

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
        )


        # открываем сайт для получения cookies
        page.goto(
            "https://rabotavdodo.ru/Lukhovitsy/eec89bd2a31db46311eedc5e2260fa4f/4254ceb0edc5826d11eff2ad492b901d",
            wait_until="domcontentloaded",
            timeout=60000
        )

        time.sleep(10)


        cookies = page.context.cookies()

        print("COOKIES:")
        print(cookies)


        session = requests.Session()

        for c in cookies:
            session.cookies.set(
                c["name"],
                c["value"],
                domain=c["domain"]
            )


        headers = {
            "User-Agent": page.evaluate("navigator.userAgent"),
            "Referer": "https://rabotavdodo.ru/"
        }


        r = session.get(
            URL,
            headers=headers
        )


        print("STATUS:", r.status_code)
        print(r.text[:3000])


        browser.close()



if __name__ == "__main__":
    main()
