from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///game.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Hero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    power = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Integer, default=100)
    items = db.relationship("Item", backref="owner", cascade="all, delete-orphan", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "power": self.power,
            "health": self.health,
            "items": [item.to_dict() for item in self.items],
        }

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    damage = db.Column(db.Integer, default=5)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "damage": self.damage,
        }

    # 2. Внешний ключ: хранит id героя-владельца из таблицы 'hero'
    hero_id = db.Column(db.Integer, db.ForeignKey("hero.id"), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "hui"


@app.route("/add-test")
def add_test():
    new_hero = Hero(name="Артур", power = 55, health = 100)

    db.session.add(new_hero)

    db.session.commit()

    return f"Герой {new_hero.name} был создан. Его сила: {new_hero.power}, его здоровье: {new_hero.health}"

@app.route("/heroes")
def show_heroes():
    # Достаем всех героев из базы данных:
    heroes_from_db = Hero.query.all()

    # Собираем красивую строку для проверки:
    response_text = "<h2>Список героев из базы данных:</h2><ul>"
    for h in heroes_from_db:
        response_text += (
            f"<li>ID #{h.id}: <b>{h.name}</b> | Сила: {h.power} | HP: {h.health}</li>"
        )
    response_text += "</ul>"

    return response_text

@app.route("/hit/<int:hero_id>/<int:damage>")
def hit_hero(hero_id, damage):
    hero = Hero.query.get_or_404(hero_id)

    hero.health -= damage

    db.session.commit()

    return f"По герою {hero.name} (ID #{hero.id}) нанесен урон {damage}! Теперь его HP: {hero.health}"


@app.route("/make-mage")
def make_mage():
    new_mage = Hero(name="Гендальф", power=90, health=100)

    db.session.add(new_mage)

    db.session.commit()

    return f"Маг сохранен"

@app.route("/find-hero/<int:hero_id>")
def find_hero(hero_id):
    hero = Hero.query.get(hero_id)

    if hero == None:
        return "Герой не найден"
    else:
        return f"Найден герой {hero.name}, его сила: {hero.power}"

@app.route("/buff/<int:hero_id>")
def buff(hero_id):
    hero = Hero.query.get(hero_id)
    if hero == None:
        return "Герой не найден"
    else:
        hero.power += 10
        db.session.commit()
        return f"Герой {hero.name} прокачан! Его сила: {hero.power}"

@app.route("/delete/<int:hero_id>")
def hero_delete(hero_id):
    hero = Hero.query.get(hero_id)
    if hero == None:
        return "Герой не найден"
    else:
        db.session.delete(hero)
        db.session.commit()
        return f"Герой {hero.name} удален"

@app.route("/find-by-name/<name>")
def find_name(name):
    hero = Hero.query.filter_by(name=name).first()
    if hero == None:
        return "Герой не найден"
    else:
        return f"Найден {hero.name}! Его ID: #{hero.id}, сила: {hero.power}"

@app.route("/strong/<int:power_lvl>")
def find_power(power_lvl):
    hero = Hero.query.filter_by(power=power_lvl).all()
    if not hero:
        return "Герои не найдены"
    else:
        return f"Найдено героев с силой {power_lvl}: {len(hero)} шт."

    
@app.route("/alive")
def alive():
    alive_heroes = Hero.query.filter(Hero.health>0).all()
    if not alive_heroes:
        return "Хуйня вась"
    else:
        return f"В живых осталось: {len(alive_heroes)} бойцов"

@app.route("/hospital")
def hospital():
    wounded = Hero.query.filter((Hero.health > 0) & (Hero.health < 80)).all()
    if not wounded:
        return "Все бойцы здоровы"
    else:
        return f"В госпитале лежат: {len(wounded)} бойцов"

@app.route("/leaderboard")
def leaderboard():
    top_hero = Hero.query.order_by(Hero.power.desc()).first()
    if not top_hero:
        return "На арене пока нет ни одного бойца!"
    else:
        return f"Топ-1 боец арены: {top_hero.name} с силой {top_hero.power}!"

@app.route("/give-sword/<int:hero_id>")
def give_sword(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        return "Нет такого героя"
    else:
        sword = Item(title="Стальной меч", damage = 15, owner = hero)
        db.session.add(sword)
        db.session.commit()
        return f"Герою {hero.name} успешно выдан меч!"

@app.route("/inventory/<int:hero_id>")
def show_inventory(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        return "Герой не найден"
    else:
        if not hero.items:
            return "Инвентарь пуст"
        else:
            items_list = [f"{item.title} (урон: {item.damage})" for item in hero.items]
            return f"Список предметов: {', '.join(items_list)}"

@app.route("/api/hero/<int:hero_id>")
def api_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if not hero:
        return jsonify({"error": "Герой не найден"}), 404
    else:
        return jsonify(hero.to_dict())

@app.route("/api/heroes")
def show_all_heroes():
    heroes = Hero.query.all()
    heroes_list = [hero.to_dict() for hero in heroes]
    return jsonify(heroes_list)


if __name__ == "__main__":
    app.run(debug=True)