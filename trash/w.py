class Hero:
    # Метод __init__ (инициализатор) запускается автоматически, когда мы создаем героя.
    # Слово self означает "я сам". Оно привязывает характеристики к конкретному объекту.
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, target):
        print(f"{self.name} аттаковал {target.name} и наносит {self.damage} урона")
        target.hp = target.hp - self.damage

    def heal(self, amount):
        print(f"Здоровье {self.name} исцелено на {amount}")
        self.hp = self.hp + amount

axe = Hero('axe', 780, 55)
pudge = Hero('pudge', 800, 75)

print(f"Здоровье пуджа: {pudge.hp}")

axe.attack(pudge)

print(f"Здоровье Пуджа после атаки: {pudge.hp}")

pudge.heal(30)

print(pudge.hp)