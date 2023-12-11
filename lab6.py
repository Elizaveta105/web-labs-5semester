from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, session, redirect
import psycopg2

lab6=Blueprint('lab6', __name__)


@lab6.route("/lab6/")
def