import json

# Это строка, пришедшая с сервера
game_data_json = '{"game": "Counter-Strike 2", "status": "playing", "winrate": 48}'

# 1. Преврати строку game_data_json в словарь Python (вспомни Задачу 1)
my_game = json.loads(game_data_json)

# 2. Обратись к ключу 'winrate' в словаре и перезапиши его значение на 51
my_game['winrate'] = 51

# 3. Преврати обновленный словарь my_game обратно в строку (вспомни Задачу 2)
updated_json = json.dumps(my_game)

# 4. Выведи финальный текст на экран
print(updated_json)