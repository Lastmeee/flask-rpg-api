import sqlite3

connection = sqlite3.connect("cs_inventory.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM cs_inventory WHERE price > 10000")

skin_info = cursor.fetchall()

print("Скины: ")

for skin in skin_info:
    print(f"[{skin[0]}] Оружие {skin[1]} Скин: {skin[2]} Цена: {skin[3]}")

connection.close()