import requests

# 1. Указываем адрес (URL) сервера
url = "https://official-joke-api.appspot.com/random_joke"

print("Отправляем запрос к серверу...")

# 2. Делаем GET-запрос (GET означает "дай мне данные")
response = requests.get(url)

# 3. Берем ответ сервера и сразу превращаем его в словарь Python
data = response.json()

# 4. Выводим полученные данные
# (Сервер присылает словарь с ключами 'setup' и 'punchline')
print("-" * 20)
print(f"Заход: {data['setup']}")
print(f"Панчлайн: {data['punchline']}")
print("-" * 20)