import requests
import json
import os
from datetime import datetime


CITY_ID = "eec89bd2a31db46311eedc5e2260fa4f"

CITY_NAME = "Луховицы"


API_URL = (
    "https://rabotavdodo.ru/api/dodois/vacancies"
    f"?localities={CITY_ID}"
    "&staffTypes=Courier"
)


def get_vacancies():

    session = requests.Session()

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }


    response = session.get(
        API_URL,
        headers=headers,
        timeout=30
    )


    print("STATUS:", response.status_code)

    response.raise_for_status()

    return response.json()



def main():

    print(
        "START",
        datetime.now()
    )


    try:

        data = get_vacancies()


        print(
            json.dumps(
                data,
                ensure_ascii=False,
                indent=2
            )
        )


    except Exception as e:

        print(
            "ERROR:",
            e
        )



if __name__ == "__main__":
    main()
