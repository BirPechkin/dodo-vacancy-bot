import os
import asyncio
from playwright.async_api import async_playwright

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://rabotavdodo.ru/Zaraysk?tabSlug=delivery"

async def get_page_text():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        await page.goto(
            URL,
            wait_until="networkidle",
            timeout=60000
        )

        text = await page.locator("body").inner_text()

        await browser.close()

        return text

async def main():
    text = await get_page_text()

    print(text[:1000])

asyncio.run(main())
