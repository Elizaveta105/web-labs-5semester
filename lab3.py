from flask import Blueprint, render_template, request
lab3 = Blueprint ('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user') # Получение имени пользователя из запроса
    if user == '':
        errors['user'] = 'Заполните поле!' # Валидация поля user
    
    age = request.args.get('age') # Получение возраста
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex') # Получение пола пользователя
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors) 


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    # Пусть кофе стоит 120 рублей, чёрный чай — 80 рублей, зелёный — 70 рублей
    if drink == 'cofee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара — на 10
    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}
    surname = request.args.get('surname')
    if surname == '':
        errors['surname'] = 'Заполните поле!'

    name = request.args.get('name')
    if name == '':
        errors['name'] = 'Заполните поле!'

    middlename = request.args.get('middlename')
    if middlename == '':
        errors['middlename'] = 'Заполните поле!'
    
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    start = request.args.get('start')
    if start == '':
        errors['start'] = 'Заполните поле!'

    finish = request.args.get('finish')
    if finish == '':
        errors['finish'] = 'Заполните поле!'

    data = request.args.get('data')
    if data == '':
        errors['data'] = 'Заполните поле!'

    luggage = request.args.get('luggage')

    tickettype = request.args.get('tickettype')

    polka = request.args.get('polka')

    return render_template('ticket.html', surname=surname, name=name, middlename=middlename, age=age, 
    start=start, finish=finish, data=data, luggage=luggage, tickettype=tickettype, polka=polka, errors=errors)
