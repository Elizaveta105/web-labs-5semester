from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return"""
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <h1>Меню</h1>

        <footer>
            &copy; Якунина Елизавета, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""    

@app.route("/lab1")
def lab1():
    return"""
<!doctype html>
<html>
    <head>
        <title>Якунина Елизавета Владимировна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов Werkzeug, 
            а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </h1>

        <footer>
            &copy; Якунина Елизавета, ФБИ-14, 3 курс, 2023
        </footer>
    </body>
</html>
"""

