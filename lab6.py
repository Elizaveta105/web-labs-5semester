from flask import Blueprint, request, render_template, redirect 
from Db import db
from Db.models import users, articles 
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user

lab6=Blueprint('lab6', __name__)


@lab6.route('/lab6/')
def lab():
    return render_template('lab6.html')


@lab6.route("/lab6/check")
def main():
    my_users = users.query.all()
    print(my_users)
    return "result in console!"


@lab6.route("/lab6/checkarticles")
def checkarticles():
    all_articles = articles.query.all()
    print(all_articles)
    return "result in console!"



