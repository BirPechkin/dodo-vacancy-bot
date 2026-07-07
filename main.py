import requests

url = "https://rabotavdodo.ru/api/dodois/get-pizzeria-by-vacancy?localities=ca2ee3d72c08bfa111efbd700111a8ac&locale=ru&staffTypes=Courier"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://rabotavdodo.ru/Zaraysk?tabSlug=delivery",
    "Accept": "*/*"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text[:1000])
