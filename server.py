from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
