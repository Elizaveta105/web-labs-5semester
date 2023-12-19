from flask import Blueprint, render_template, request, abort

lab8 = Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')


courses = [
    {"name": "c++", "videos": 3, "price": 3000},
    {"name": "basic", "videos": 30, "price": 0},
    {"name": "c#", "videos": 8}
]


@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return courses


@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_course(course_num):
    if course_num < 0 or course_num >= len(courses):  # Проверяем, принадлежит ли course_num корректному диапазону
        abort(404)
    return courses[course_num]