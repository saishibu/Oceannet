from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('newLogin.html')
    else:
        return "Hello"

# @app.route('/mainPage')
# def mainPage():
#     return render_template('index2.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
        return redirect(url_for('mainPage'))
    else:
        flash('wrong password!')
        return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)

app.run(debug=True,port=5000)