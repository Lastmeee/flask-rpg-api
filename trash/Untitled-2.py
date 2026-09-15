import sqlite3

connection = sqlite3.connect ("databaz.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS databaz (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               profession TEXT)
""")

print("Таблица создана")

cursor.execute("INSERT INTO databaz (name, age, profession) VALUES ('Вика', 12, 'Ученик')")
cursor.execute("INSERT INTO databaz (name, age, profession) VALUES ('Ваня', 18, 'Студент')")

connection.commit()

connection.close()

print("Данные внесены")