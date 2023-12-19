from flask import Blueprint, render_template, request, redirect, url_for

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        friend_name = request.form.get('friend_name')
        friend_gender = request.form.get('friend_gender')
        sender_name = request.form.get('sender_name')
        return redirect(url_for('lab9.pozdravlenie', friend_name=friend_name, friend_gender=friend_gender, sender_name=sender_name))
    else:
        return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('lab9/error.html'), 404


@lab9.app_errorhandler(500)
def internal_server_error(e):
    return render_template('lab9/error2.html'), 500


@lab9.route('/lab9/500')
def trigger_error():
    1/0


@lab9.route('/lab9/pozdravlenie', methods=['GET'])
def pozdravlenie():
    friend_name = request.args.get('friend_name')
    friend_gender = request.args.get('friend_gender')
    sender_name = request.args.get('sender_name')
    return render_template('lab9/pozdravlenie.html', friend_name=friend_name, friend_gender=friend_gender, sender_name=sender_name)