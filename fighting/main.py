from flask import Flask, render_template, request

app = Flask(__name__)

heroes_db = []
enemies_db = []

class Hero:
    def __init__(self, h_name, h_role, h_power):
        self.h_name = h_name
        self.h_role = h_role
        self.h_power = h_power
        h_health = 100

class Enemy:
    def __init__(self, e_name, e_power):
        self.e_name = e_name
        self.e_power = e_power
        e_health = 100

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/create_hero", methods=["GET", "POST"])
def create_hero():
    if request.method == "POST":
        h_name = request.form["hero_name"]
        h_role = request.form["hero_role"]
        h_power = int(request.form["hero_power"])

        hero = Hero(h_name, h_role, h_power)

        heroes_db.append(hero)
        return render_template("finish_create.html", hero=hero)

    return render_template("create_hero.html")

@app.route("/heroes")
def show_heroes():
    return render_template("list_heroes.html", heroes = heroes_db)

@app.route("/create_enemy", methods=["POST", "GET"])
def create_enemy():
    if request.method == "POST":
        e_name = request.form["enemy_name"]
        e_power = request.form["enemy_power"]

        enemy = Enemy(e_name, e_power)

        enemies_db.append(enemy)

        return render_template("finish_create_enemy.html", enemy=enemy)

    return render_template("create_enemy.html")


@app.route("/enemies")
def show_enemies():
    return render_template("list_enemies.html", enemies=enemies_db)

@app.route("/arena", methods = ["POST", "GET"])
def arena():
    if request.method == "POST":
        return render_template("arena.html", heroes = heroes_db, enemies = enemies_db)

if __name__ == "__main__":
    app.run(debug=True)