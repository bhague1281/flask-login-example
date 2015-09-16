import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask.ext.login import LoginManager, login_required, current_user, login_user, logout_user
from flask.ext.bcrypt import Bcrypt
from models import *

app = Flask(__name__)
app.secret_key = 'alsdkfjalsdkfjalskdfjs'
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
  return User.objects.get(id=user_id)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    try:
      user = User.objects.get(username=request.form['username'])
    except:
      flash({
        'type': 'danger',
        'message': 'Username and/or password is incorrect'
        })
      return redirect(url_for('login'))

    if user and bcrypt.check_password_hash(user.password, request.form['password']):
      login_user(user)
      flash({
        'type': 'success',
        'message': '{} logged in successfully!'.format(user.username)
        })
      return redirect(url_for('secret'))
    else:
      flash({
        'type': 'danger',
        'message': 'Username and/or password is incorrect'
        })
      return redirect(url_for('login'))
  return render_template('login.html')

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
  if request.method == 'POST':
    User(username=request.form['username'],
         password=bcrypt.generate_password_hash(request.form['password'])).save()
    flash({
      'type': 'success',
      'message': 'User {} has been created!'.format(request.form['username'])
      })
    return redirect(url_for('login'))
  return render_template('register.html')

@app.route('/secret')
@login_required
def secret():
  return render_template('secret.html')

@app.route("/auth/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=os.environ.get('PORT', 5000))