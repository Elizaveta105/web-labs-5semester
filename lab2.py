from flask import Blueprint, render_template
# Указали, что из пакета flask нам нужен класс Flask
# url_for() возвращает нужный нам путь в виде строки
# render_template() из пакета flask отвечает за рендеринг шаблонов (создание html-текста для браузера)
# Нам нужно создать не приложение Flask, а эскиз, поэтому поменяем Flask на Blueprint
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/example')
def example():
    name = 'Елизавета Якунина'
    group = 'ФБИ-14'
    course = '3 курс'
    lr_number = 'Лабораторная работа 2'

    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
    ]

    books =[
        {'book': 'Властелин колец', 'author': 'Джон Р. Р. Толкин', 'genre': 'Фэнтези', 'pages': 1120},
        {'book': 'Унесенные ветром', 'author': 'Маргарет Митчелл', 'genre': 'Классика', 'pages': 992},
        {'book': '11/22/63', 'author': 'Стивен Кинг', 'genre': 'Фантастика', 'pages': 800},
        {'book': 'Лекарь. Ученик Авиценны', 'author': 'Ной Гордон', 'genre': 'Приключения', 'pages': 816},
        {'book': 'К востоку от Эдема', 'author': 'Джон Стейнбек', 'genre': 'Классика', 'pages': 768},
        {'book': 'Мидлмарч', 'author': 'Джордж Элиот', 'genre': 'Классика', 'pages': 832},
        {'book': 'Волхв', 'author': 'Джон Фаулз', 'genre': 'Приключения', 'pages': 816},
        {'book': 'Столпы Земли', 'author': 'Кен Фоллетт', 'genre': 'Приключения', 'pages': 880},
        {'book': 'Ярмарка тщеславия', 'author': 'Уильям Теккерей', 'genre': 'Роман', 'pages': 752},
        {'book': 'Отверженные', 'author': 'Виктор Гюго', 'genre': 'Проза', 'pages': 1284},
        {'book': 'Американская трагедия', 'author': 'Теодор Драйзер', 'genre': 'Классика', 'pages': 800}
    ]

    return render_template('example.html', name=name, group=group, 
                           course=course, lr_number=lr_number, 
                           fruits=fruits, books=books)

@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')

@lab2.route('/lab2/kartinki')
def kartinki():
    return render_template('kartinki.html')
