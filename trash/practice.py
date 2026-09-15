import sqlite3

connection = sqlite3.connect("cs_inventory.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cs_inventory (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               weapon TEXT,
               skin_name TEXT,
               price INT)
""")

print("Таблица создана")

cursor.execute("INSERT INTO cs_inventory (weapon, skin_name, price) VALUES ('AK-47', 'Azimov', 300)")
cursor.execute("INSERT INTO cs_inventory (weapon, skin_name, price) VALUES ('AWP', 'Dragon lore', 150000)")
cursor.execute("INSERT INTO cs_inventory (weapon, skin_name, price) VALUES ('Desert Eagle', 'Potoc information', 10000)")

connection.commit()
connection.close()

print("Соединение закрыто")
