contacts = []

def create_user(name, telephone):
    user = {
        "name": name,
        "phone": telephone
    }
    contacts.append(user)

def check_users():
    if len(contacts) == 0:
        print ("Список пуст")
    else:
        for user in contacts:
            print(f"{user['name']}: {user['phone']}")

def find_user(temp_name):
    for user in contacts:
        if user['name'] == temp_name:
            return (user['phone'])
    return ("Пользователь не найден")   
        
def delete_user(temp_name):
    for user in contacts:
        if temp_name == user['name']:
            contacts.remove(user)
            return "Пользователь удален"
    return "Пользователь не найден"


while True:
    print("1. Создать пользователя")
    print("2. Список пользователей")
    print("3. Поиск пользователя")
    print("4. Удаление пользователя")
    print("5. Выход")
    variant = int(input("Введите число 1-5: "))

    if variant == 1:
        new_user = input("Введите имя пользователя: ")
        new_phone = input("Введите номер телефона: ")
        create_user(new_user, new_phone)

    if variant == 2:
        check_users()

    if variant == 3:
        find_name = input("Введите имя пользователя: ")
        print(find_user(find_name))

    if variant == 4:
        delete_name = input("Введите имя пользователя: ")
        delete_user(delete_name)

    if variant == 5:
        print("Вы вышли")
        break