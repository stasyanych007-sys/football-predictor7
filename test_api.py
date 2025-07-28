import requests

url = "http://127.0.0.1:10000/api/predict"

data = {
    "home_team": "Barcelona",
    "away_team": "Real Madrid",
    "home_xg": 1.8,
    "away_xg": 1.3,
    "home_form": 3.2,
    "away_form": 2.8
}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # вызовет исключение при ошибке 4xx/5xx

    result = response.json()
    print("✅ Успешно! Ответ от API:")
    print(result)

except requests.exceptions.HTTPError as err:
    print(f"❌ Ошибка HTTP: {err}")
    if err.response is not None:
        print("Ответ сервера:", err.response.text)

except Exception as e:
    print(f"❌ Общая ошибка: {e}")
