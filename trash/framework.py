from flask import Flask

app =  Flask(__name__)

@app.route("/")
def home():
    return "Главная страница магазина"

@app.route("/contacts")
def contacrs():
    return "Наш телефон: +79990001122"

@app.route("/hello/<name>")
def hello(name):
    return (f"Привет, {name}")

@app.route("/square/<int:number>")
def square(number):
    s = number ** 2
    return (f"Квадрат числа {number} равен {s}")

@app.route("/add/<int:num1>/<int:num2>")
def summa(num1, num2):
    sum = num1 + num2
    return (f"Сумма {num1} и {num2} = {sum}")

@app.route("/age/<int:age>")
def age(age):
    if age >= 18:
        return "Совершеннолетний"
    else:
        return "Несовершеннолетний"

if __name__ == "__main__":
    app.run(debug=True)