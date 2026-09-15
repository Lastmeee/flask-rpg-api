class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.level = 1 
        self.__health = 100

    def introduce(self):
        print(f"Я {self.name}! И я - {self.role}")

    def level_up(self):
        self.level += 1
        print(f"{self.name} получил новый уровень! Теперь его уровень {self.level}")

    def attack(self, target):
        target.change_health(-20)
        print(f"{self.name} атаковал {target.name}! Теперь здоровье {target.name} = {target.get_health()}")

    def get_health(self):
        return self.__health

    def change_health(self, amount):
        self.__health += amount

class Mage(Hero):
    def heal(self, target):
        target.change_health(20)
        print(f"{target.name} был исцелен! Его здоровье = {target.get_health()}")

    def attack(self, target):
        target.change_health(-40)
        print(f"{self.name} кастует огненный шар и сносит 40 здоровья {target.name}")

def save_progress(self):
        with open ("save.txt", "w", encoding="utf-8") as file:
            file.write("Игра сохранена!\n")
            file.write("Урвоень: 5")

hero1 = Hero("Артур", "рыцарь")
hero2 = Hero("Мерлин", "маг")
enemy = Hero("Гоблин", "монстр")
hero3 = Mage("Азимут", "целитель")

print(hero1.name)
print(hero2.role)

hero1.introduce()
hero2.introduce()

hero1.level_up()

hero1.attack(enemy)

hero3.heal(hero1)

hero3.attack(enemy)


while hero1.get_health() > 0 and enemy.get_health() > 0:
    hero1.attack(enemy)
    enemy.attack(hero1)

if hero1.get_health() > 0:
    print(f"{enemy.name} потерпел поражение. {hero1.name} победитель!")
else:
    print(f"{hero1.name} потерпел поражение. {enemy.name} победитель!")


