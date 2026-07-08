from playwright.sync_api import sync_playwright

url = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier"

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        executable_path="/opt/render/.cache/ms-playwright/chromium_headless_shell-1228/chrome-headless-shell-linux64/chrome-headless-shell"
    )

    page = browser.new_page(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/146 Safari/537.36"
    )

    response = page.goto(url)

    print("STATUS:", response.status)

    print(page.content()[:2000])

    browser.close()
