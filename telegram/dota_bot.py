import telebot
import requests

# 1. Вставь сюда свой токен от BotFather (обязательно в кавычках!)
TOKEN = "8680050982:AAELM_H96IV361R6yA680dBa3pa3pQbed0Y"

# 2. Создаем объект нашего бота
bot = telebot.TeleBot(TOKEN)

# 3. Учим бота реагировать на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот для мониторинга рынка Dota 2. Готов к работе! Напиши мне точное название предмета, а я пришлю тебе цену на него")

# 4. Учим бота реагировать на любые другие текстовые сообщения
@bot.message_handler(content_types=['text'])
def search_dota_item(message):
    item_name = message.text
    bot.reply_to(message, f"Отправляю запрос к Габену, ищу {item_name}...")

    # Формируем ссылку
    url = f"https://steamcommunity.com/market/priceoverview/?appid=570&currency=5&market_hash_name={item_name}"
    
    try:
        response = requests.get(url)
        
        # Сначала проверяем код ответа сервера (200 - всё отлично)
        if response.status_code == 200:
            data = response.json()
            
            # ЗАЩИТА: проверяем, что data не пустая (не None), прежде чем использовать .get()
            if data and data.get('success') == True:
                price = data.get('lowest_price', 'Нет в продаже')
                bot.send_message(message.chat.id, f"✅ Минимальная цена на ТП: {price}")
            else:
                bot.send_message(message.chat.id, "❌ Предмет не найден. Проверь правильность написания (нужно точное английское название)!")
                
        # Если Steam ругается на слишком частые запросы
        elif response.status_code == 429:
            bot.send_message(message.chat.id, "⚠️ Steam временно заблокировал нас за спам. Подожди пару минут и попробуй снова!")
            
        # На случай других ошибок сервера
        else:
            bot.send_message(message.chat.id, f"❌ Сервер Steam вернул ошибку: {response.status_code}")
            
    except Exception as e:
        # Ловим любые системные ошибки (например, если вообще пропал интернет)
        bot.send_message(message.chat.id, "❌ Ошибка при попытке связаться с сервером.")
        print(f"Системная ошибка: {e}")