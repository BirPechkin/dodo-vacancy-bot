from playwright.sync_api import sync_playwright
import requests
import json


CITY_URL = (
    "https://rabotavdodo.ru/"
    "Lukhovitsy/"
    "eec89bd2a31db46311eedc5e2260fa4f/"
    "4254ceb0edc5826d11eff2ad492b901d"
    "?tabSlug=all"
)


API_URL = (
    "https://rabotavdodo.ru/api/dodois/vacancies"
    "?localities=eec89bd2a31db46311eedc5e2260fa4f"
    "&staffTypes=Courier"
)



def get_cookies():

    with sync_playwright() as p:

        browser = p.chromium.launch(
    headless=True,
    args=[
        "--no-sandbox",
        "--disable-dev-shm-usage"
    ]
)

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "Chrome/120 Safari/537.36"
            )
        )

        print("OPEN PAGE")

        page.goto(
            CITY_URL,
            wait_until="networkidle",
            timeout=60000
        )

        cookies = page.context.cookies()

        print("COOKIES:", len(cookies))

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
            "User-Agent":
            "Mozilla/5.0"
        },
        timeout=30
    )


    print("STATUS:", response.status_code)


    try:
        data = response.json()

        print(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            )
        )

    except Exception:
        print(response.text)



if __name__ == "__main__":
    main()
