from flask import Blueprint, render_template, request
lab3 = Blueprint ('lab3', __name__)


@lab3.route('/lab3/form1')
def form1():
    user = request.args.get('user') # Получение имени пользователя из запроса
    age = request.args.get('age') # Получение возраста
    sex = request.args.get('sex') # Получение пола пользователя
    return render_template('form1.html', user=user, age=age, sex=sex) 
