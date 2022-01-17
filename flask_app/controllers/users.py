from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.user import User


@app.route('/')
def all():
    return render_template('all_users.html', users=User.get_all())


@app.route('/create_users', methods=['get', 'post'])
def new_user():
    if request.method == 'get':
        return redirect('/')
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'ema': request.form['ema']
    }
    User.save(data)
    return redirect('/')


@app.route('/add_user')
def create_user():
    return render_template('add_user.html')


@app.route('/users/<int:id>')
def show_one(id):
    data = {
        'id': id,
    }
    return render_template('one_user.html', user=User.get_one(data))


@app.route('/users/<int:id>/update_page')
def update_page(id):
    data = {
        'id': id,
    }
    return render_template('edit.html', user=User.get_one(data))


@app.route('/users/<int:id>/update', methods=['post'])
def update_user(id):
    data = {
        'id': id,
        'fname': request.form['fname'],
        'lname': request.form['lname'],
        'ema': request.form['ema'],
    }
    User.update(data)
    return redirect('/')


@app.route('/users/<int:id>/delete', methods=['post'])
def delete_user(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')
