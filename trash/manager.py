import json

class ContactManager:
    # Метод __init__ сработает автоматически при создании менеджера
    def __init__(self):
        # Теперь список контактов принадлежит конкретному объекту менеджера
        self.contacts = []
        # При создании менеджера сразу загружаем данные
        self.load_contacts()

    def save_contacts(self):
        with open('contacts.json', 'w', encoding='utf-8') as file:
            # Обрати внимание: теперь мы везде обращаемся к self.contacts
            json.dump(self.contacts, file, ensure_ascii=False, indent=4)

    def load_contacts(self):
        try:
            with open('contacts.json', 'r', encoding='utf-8') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    # --- ТВОЯ ЗАДАЧА: заполнить методы ниже ---

    def create_user(self, name, telephone):
        user = {
            "name": name,
            "phone": telephone
        }
        self.contacts.append(user)
        self.save_contacts()
        pass

    def check_users(self):
        if len(self.contacts) == 0:
            print("Список пуст")
        else:
            for user in self.contacts:
                # Используем квадратные скобки, так как user — это словарь
                print(f"{user['name']}: {user['phone']}")

    def find_user(self, temp_name):
        for user in self.contacts:
            if user['name'] == temp_name:
                return user['phone']
        return "Пользователь не найден"

    def delete_user(self, temp_name):
        for user in self.contacts:
            if user['name'] == temp_name:
                self.contacts.remove(user) # Удаляем словарь целиком из списка
                self.save_contacts()       # Сохраняем изменения в файл
                return "Пользователь удален"
        return "Пользователь не найден"