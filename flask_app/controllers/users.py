from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def create_user():
    return render_template('form1.html')


@app.route('/create_users', methods=['post'])
def new_user():
    data = {
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'ema': request.form['ema']
    }
    User.save(data)
    return redirect('/allusers')


@app.route('/allusers')
def all():
    return render_template('form2.html', users=User.get_all())
