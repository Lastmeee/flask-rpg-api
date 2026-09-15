class Player:
    def __init__(self, nickname):
        self.nickname = nickname
        self.__health = 100

    def get_health(self):
        return self.__health
        pass

    def heal(self, amount):
        self.__health += amount
        if self.__health > 100:
            self.__health = 100
        print(f"Игрок {self.nickname} подлечился. Его хп = {self.__health}") 
        pass

# --- ТЕСТИРОВАНИЕ ---
me = Player("Lastmeee")

# Пытаемся сломать систему (спойлер: Питон просто создаст новую левую переменную, 
# а настоящее приватное здоровье останется нетронутым)
me.__health = 50000 

# Лечимся легально
me.heal(50)

# Смотрим реальное ХП
print(f"Реальное здоровье: {me.get_health()}")