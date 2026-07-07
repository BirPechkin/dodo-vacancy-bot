import requests

URL = "https://rabotavdodo.ru/api/dodois/vacancies?localities=ca2ee3d72c08bfa111efbd700111a8ac&staffTypes=Courier"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://rabotavdodo.ru/Zaraysk?tabSlug=delivery",
    "Accept": "application/json"
}

response = requests.get(URL, headers=headers)

print("STATUS:", response.status_code)
print(response.text[:2000])
