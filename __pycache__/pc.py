class Laptop:
    def __init__(self, model, cpu, gpu, ram):
        self.model = model
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

    def show_specs(self):
        print(f"Ноутбук {self.model}:")
        print(f"Процессор: {self.cpu}")
        print(f"Видеокарта: {self.gpu}")
        print(f"ОЗУ: {self.ram}")
        print("-" * 20)

    def run_game(self, game_name):
        print(f"Запускаем {game_name}... Видеокарта {self.gpu} выдает стабильный FPS!")

    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        print(f"Оперативная память успешно обновлена до {new_ram}")

# Создаем объект ноутбука
my_pc = Laptop("Asus ROG Strix Scar 15", "Ryzen 9", "RTX 3080", "2 плашки по 8 ГБ 3200 МГц")

# Выводим характеристики
my_pc.show_specs()

my_pc.run_game("path of exile")

my_pc.upgrade_ram(32)

my_pc.show_specs()