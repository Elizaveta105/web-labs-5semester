from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

# Главная страница - список объявлений
@app.route('/')
def index_rgz():
    ads = Ad.query.all()
    return render_template('index_rgz.html', ads=ads)
