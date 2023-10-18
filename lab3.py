from flask import Blueprint, render_template, request
lab3 = Blueprint ('lab3', __name__)


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
