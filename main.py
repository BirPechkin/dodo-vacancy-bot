import os
import requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

URL = "https://rabotavdodo.ru/Zaraysk?tabSlug=delivery"

KEYWORDS = [
    "курьер",
    "водитель",
    "автомобил",
    "личн"
]

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=data)

def check_vacancy():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    page_text = soup.get_text(" ").lower()

    found = []

    for word in KEYWORDS:
        if word in page_text:
            found.append(word)

    if found:
        send_message(
            "🍕 Додо Зарайск\n"
            "Нашёл признаки вакансии!\n\n"
            "Найдено: " + ", ".join(found) +
            "\n\n" + URL
        )
    else:
        send_message(
            " Что видит бот на странице:\n\n"
            + page_text[:500]
        )

check_vacancy()
