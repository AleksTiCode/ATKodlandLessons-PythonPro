from flask import Flask, render_template
from random import choice
import string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fact")
def facts():
    programming_facts = [
    "Первый программист в истории — Ада Лавлейс, которая работала над аналитической машиной Чарльза Бэббиджа.",
    "Язык программирования Python был создан Гвидо ван Россумом в конце 1980-х годов.",
    "Первая программа, написанная на языке C, была создана в 1972 году.",
    "Термин 'баг' (bug) в программировании возник из-за того, что в 1947 году в компьютере Mark II нашли настоящую моль.",
    "JavaScript был создан за 10 дней в 1995 году и изначально назывался Mocha.",
    "Существует более 700 языков программирования, но наиболее популярными являются Java, Python и JavaScript.",
    "Git, система контроля версий, была создана Линусом Торвальдсом в 2005 году.",
    "Фреймворк Django, используемый для веб-разработки на Python, был создан в 2003 году.",
    "Алгоритм сортировки пузырьком (Bubble Sort) был разработан в 1956 году и считается одним из самых простых, но неэффективных алгоритмов.",
    "Программирование может улучшить навыки решения проблем и логического мышления."
    ]
    return render_template("fact.html", fact=choice(programming_facts))

@app.route("/password")
def password():
    password = ''.join(choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(10))
    return render_template("password.html", password=password)

app.run(debug=True)