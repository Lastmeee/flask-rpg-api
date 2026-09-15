from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Класс героя
class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.level = 1
        self.health = 100

# Класс монстра
class Monster:
    def __init__(self, name, monster_type):
        self.monster_type = monster_type
        self.name = name
        self.health = 100

@app.route("/")
def home():
    return "Главная страница игры"

@app.route("/create", methods=["GET", "POST"])
def create_hero():
    if request.method == "POST":
        name = request.form["hero_name"]
        role = request.form["hero_role"]
        # Забираем силу из формы
        power = int(request.form["power"])

        hero = Hero(name, role)

        # Перенаправляем с двумя параметрами
        return redirect(url_for("hero_stats", hero_name=name, power=power))

    return render_template("create.html")

@app.route("/create-enemy", methods=["POST", "GET"])
def create_enemy():
    enemy = None
    if request.method == "POST":
        name = request.form["monster_name"]
        monster_type = request.form["monster_type"]

        enemy = Monster(name, monster_type)

    return render_template("enemy.html", enemy=enemy)

# ИСПРАВЛЕНИЕ ТУТ: принимаем power и в URL, и в аргументах функции!
@app.route("/hero/<hero_name>/<int:power>")
def hero_stats(hero_name, power):
    return render_template("arena.html", hero_name=hero_name, power=power)

@app.route("/roster")
def show_roster():
    heroes = [
    Hero("Артур", "Рыцарь"),
    Hero("Мерлин", "Маг"),
    Hero("Ланселот", "Паладин")
]
    return render_template("roster.html", heroes = heroes)

if __name__ == "__main__":
    app.run(debug=True)