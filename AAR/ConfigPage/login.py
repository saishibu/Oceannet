#!/usr/bin/python
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os,pymysql
pwd=str(os.getcwd())
print(pwd)
app = Flask(__name__)

@app.route('/')
def home():

    if not session.get('logged_in'):
        return render_template('newLogin.html')
    else:
        return render_template('index.html')

@app.route('/mainPage')
def mainPage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'amma' and request.form['username'] == 'on':
        session['logged_in'] = True
        return redirect(url_for('mainPage'))
    else:
        flash('wrong password!')
        #return redirect(url_for('home'))
        return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    print(pwd)

@app.route('/configIP', methods=['POST'])
def configIP():
    cpeIP = request.form['CPEIP'] 
    boatName = request.form['boatName']
    data={'cpeIP':cpeIP,'boatName':boatName}    
    print(data)
    try:
        conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
        cur=conn.cursor()
        cur.execute("TRUNCATE TABLE boat_data;")
        cur.execute("INSERT INTO boat_data (boatName, cpeIP) VALUES (%(boatName)s, %(cpeIP)s);",data)
        conn.commit()
        conn.close()
        flash('Saved Successfully')
    except:
        flash('Error Saving Configurations')
    return redirect(url_for('mainPage'))

@app.route('/AARTest', methods=['POST'])
def AARTest():
    cmd=os.getcwd()
    cmd=str(cmd)+"/Rotatetest.py"
    os.system(cmd)
    
    flash ('AAR Test Initiated')
    return redirect(url_for('mainPage'))

@app.route('/LEDTest', methods=['POST'])
def LEDTest():
    
    cmd=os.getcwd()
    cmd=str(cmd)+"/LEDtest.py"
    os.system(cmd)
    
    flash ('LED Test Initiated')
    return redirect(url_for('mainPage'))

app.run(debug=True,host="0.0.0.0")