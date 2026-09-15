import sqlite3

connection = sqlite3.connect("cs_inventory.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM cs_inventory WHERE skin_name = 'Potoc information'")
connection.commit()

connection.close()