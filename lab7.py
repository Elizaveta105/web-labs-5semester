from flask import Blueprint, render_template, request, abort

lab7 = Blueprint('lab7', __name__)


@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')


@lab7.route('/lab7/drink')
def drink():
    return render_template('lab7/drink.html')


@lab7.route('/lab7/api', methods = ['POST'])
def api():
    data = request.json  # Выделение JSON

    if data ['method'] == 'get-price':
        return get_price(data['params'])
    
    if data ['method'] == 'pay':
        return pay(data['params'])
    
    if data['method'] == 'refund': 
        return cancellation(data['params'])

    abort(400)  # Возврат ошибки при выыводе нестандартного метода


def get_price(params):  # Функция получения цены
    return {"result": calculate_price(params), "error": None}  
# Здесь у нас результат расчёта возвращается в поле result. И, т.к. ошибки нет,
# то в поле error будет None, которое в json преобразуется в null.


def calculate_price(params):
    drink = params['drink']
    milk = params['milk']
    sugar = params['sugar']

    # Пусть кофе стоит 120 рублей, чёрный чай — 80 рублей, зелёный — 70 рублей
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    # Добавка молока удорожает напиток на 30 рублей, а сахара — на 10
    if milk:
        price += 30
    if sugar:
        price += 10

    return price


def pay(params):  
    card_num = params['card_num']  # Проверка номера карты
    if len(card_num) != 16 or not card_num.isdigit():
        return {"result": None, "error": "Неверный номер карты"}
    
    cvv = params['cvv']  # Проверка кода CVV/CVC
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV/CVC"}
    
    price = calculate_price(params)
    return {"result": f'С карты {card_num} списано {price} руб.', "error": None}


def cancellation(params):
    card_num = params['card_num']
    if len(card_num) != 16 or not str(card_num).isdigit():
        return {"result": None, "error": "Неверный номер карты"}

    cvv = params['cvv']
    if len(cvv) != 3 or not cvv.isdigit():
        return {"result": None, "error": "Неверный номер CVV/CVC"}

    return {"result": f'<span style="color: green;">Возврат денег на карту успешно завершен!</span>', "error": None}

