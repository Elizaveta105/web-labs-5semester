from flask import Blueprint, render_template, request
lab4=Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors = {}

    if request.method == 'GET':
        return render_template('login.html', errors=errors)

    username = request.form.get('username')
    password = request.form.get('password')

    if username == '':
        errors['username'] = 'Не введен логин!'

    if password == '':
        errors['password'] = 'Не введен пароль!'

    if username == 'alex' and password == '123':
        return render_template('success2.html', username=username, password=password)
    
    elif username != '' and password != '':
        error = 'Неверные логин и/или пароль'
        return render_template('login.html', error=error, errors=errors, username=username, password=password)
    return render_template('login.html', errors=errors, username=username, password=password)


@lab4.route('/lab4/success2')
def success():
    return render_template('success2.html')


@lab4.route('/lab4/fridge', methods = ['GET', 'POST'])
def fridge():
    errors = {}
    snow = {}

    if request.method == 'GET':
        return render_template('fridge.html', errors=errors)

    temp = request.form.get('temp')
    if temp == '':
        errors['temp'] = 'Ошибка: не задана температура'
        snow = ''
    else:
        temp = int(temp)
        if temp < -12:
            errors['temp'] = 'Не удалось установить температуру — слишком низкое значение'
            snow = ''
        elif temp > -1:
            errors['temp'] = 'Не удалось установить температуру — слишком высокое значение'
            snow = ''
        else:
            if -12 <= temp <= -9:
                errors['temp'] = f'Установлена температура: {temp}\u2103'
                snow = ' \u2744\u2744\u2744'
            elif -8 <= temp <= -5:
                errors['temp'] = f'Установлена температура: {temp}\u2103'
                snow = ' \u2744\u2744'
            elif temp -4 <= temp <= -1:
                errors['temp'] = f'Установлена температура: {temp}\u2103'
                snow = ' \u2744'
    return render_template('temperatura.html', errors=errors, temp=temp, snow=snow)


@lab4.route('/lab4/zerno', methods = ['GET', 'POST'])
def zerno():
    errors = {}

    if request.method == 'GET':
        return render_template('zerno.html', errors=errors)

    weight = request.form.get('weight')
    if weight == '':
        errors['weight'] = 'Не введен вес'
    else:
        weight = int(weight)
        if weight <= 0:
            errors['weight'] = 'Неверное значение веса'
        elif weight > 500:
            errors['weight'] = "Такого объёма сейчас нет в наличии"
            
    price = 0
    price = float(price)
    zerno = request.form.get('zerno')
    if zerno == 'barley':
        price = 12000 * weight
    elif zerno == 'oats':
        price = 8500 * weight
    elif zerno == 'wheat':
        price = 8700 * weight
    else:
        price = 14000 * weight
    if weight > 50:
        price = price - (price * 0.1)
        skidka = f"Применена скидка 10% за большой объём ({price * 0.1}) руб."
    else:
        skidka = ""

    return render_template('zerno.html', weight=weight, zerno=zerno, price=price, errors=errors, skidka=skidka)


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    errors = []
    if request.method == 'GET':
        return render_template('cookies.html', errors=errors)
    
    color = request.form.get('color')
    backgroundcolor = request.form.get('backgroundcolor')

    if color == backgroundcolor:
        errors.append("Цвет текста не должен совпадать с текстом фона")

    fontsize = request.form.get('fontsize')
    if not fontsize:
        errors.append("Не задан размер текста")
    else:
        fontsize=int(fontsize)
        if fontsize < 5 or fontsize > 30:
            errors.append("Размер текста должен быть от 5px до 30px")
    if errors:
        return render_template('cookies.html', errors=errors)  
      
    headers = {
        'Set-Cookie': ['color=' + color + '; path=/', 'backgroundcolor=' + backgroundcolor + '; path=/', 
                       'fontsize=' + str(fontsize) + '; path=/'],        
        'Location': '/lab4/cookies'
    }

    return '', 303, headers
