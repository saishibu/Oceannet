#!/usr/bin/python
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
pwd=str(os.getcwd())
print(pwd)
app = Flask(__name__)

@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('newLogin.html')
    else:
        return render_template('index2.html')

@app.route('/mainPage')
def mainPage():
    return render_template('index2.html')

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
    print(pwd)


app.run(debug=True)