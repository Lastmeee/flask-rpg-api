# 1. Импортируем сам класс
from trash.manager import ContactManager

# 2. Создаем объект менеджера (при этом автоматически сработает __init__ и загрузит файл!)
manager = ContactManager()

while True:
    print("\n1. Создать пользователя")
    print("2. Список пользователей")
    print("3. Поиск пользователя")
    print("4. Удаление пользователя")
    print("5. Выход")

    try:
        variant = int(input("Введите число 1-5: "))
    except ValueError:
        print("Вы ввели не число!")
        continue

    if variant == 1:
        new_user = input("Введите имя пользователя: ")
        new_phone = input("Введите номер телефона: ")
        # 3. Вызываем методы через наш объект manager
        manager.create_user(new_user, new_phone)

    elif variant == 2:
        manager.check_users()

    elif variant == 3:
        find_name = input("Введите имя пользователя: ")
        print(manager.find_user(find_name))

    elif variant == 4:
        delete_name = input("Введите имя пользователя: ")
        print(manager.delete_user(delete_name))

    elif variant == 5:
        print("Вы вышли")
        break