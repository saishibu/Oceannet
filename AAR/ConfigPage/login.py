#!/usr/bin/python
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os,pymysql, getOTP

class Captchastore():
    captcha = None

captchadata = Captchastore()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def home():
    captcha = getOTP.generate_captcha()
    print(captcha)
    captchadata.captcha=captcha

    if not session.get('logged_in'):
        return render_template('newLogin.html',captcha=captcha)
    else:
        return render_template('index.html')

@app.route('/mainPage')
def mainPage():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    
    conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
    cur=conn.cursor()
    cur.execute("SELECT username,password FROM register;")
    try:
        data=cur.fetchone()
        username=data[0]
        password=data[1]
    except:
        flash("User not registered")
        exit()

    if request.form['otp'] != captchadata.captcha:
        flash('Incorrect OTP')
        return home()

    if request.form['password'] == password and request.form['username'] == username:
        session['logged_in'] = True
        return redirect(url_for('mainPage'))
    else:
        flash('The username and password that you entered did not match our records. Please double-check and try again.')
        #return redirect(url_for('home'))
        return home()

@app.route('/register',methods=['POST'])
def do_register():
    return render_template('register.html')

@app.route('/postRegister',methods=['POST'])
def save_register():
    username = request.form['username'] 
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']

    if password != confirmpassword:
        flash('Password not matched')
    
    data={'username': username,'password': confirmpassword}

    try:
        conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
        cur=conn.cursor()
        cur.execute("TRUNCATE TABLE register;")
        cur.execute("INSERT INTO register (username, password) VALUES (%(username)s, %(password)s);",data)
        conn.commit()
        conn.close()
        flash('Saved Successfully')
    except:
        flash('Error Saving Configurations')


@app.route("/logout")
def logout():
    session['logged_in'] = False
    flash('Logged Out Successfully')
    return home()

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    

@app.route('/configIP', methods=['POST'])
def configIP():
    cpeIP = request.form['CPEIP'] 
    boatName = request.form['boatName']
    log = request.form['log']
    Piggyback = request.form['Piggyback']
    data={'cpeIP':cpeIP,'boatName':boatName,'Piggyback':Piggyback,'log':log}    
    
    try:
        conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
        cur=conn.cursor()
        cur.execute("TRUNCATE TABLE boat_data;")
        cur.execute("TRUNCATE TABLE config;")
        cur.execute("INSERT INTO boat_data (ssid, CPE) VALUES (%(boatName)s, %(cpeIP)s);",data)
        conn.commit()
        cur.execute("INSERT INTO config (ip, log, piggyback) VALUES (%(cpeIP)s,%(log)s, %(Piggyback)s);",data)
        conn.commit()
        conn.close()
        flash('Saved Successfully')
    except:
        flash('Error Saving Configurations')
    return redirect(url_for('mainPage'))

@app.route('/AARTest', methods=['POST'])
def AARTest():
	try:
		cmd="/home/pi/Oceannet/AAR/ConfigPage/Rotatetest.py"
		os.system(cmd)
		flash ('AAR Test Completed')
	except:
		flash("Error Testing")
	return redirect(url_for('mainPage'))

@app.route('/update', methods=['POST'])
def update():
	try:
		path='/home/pi/Oceannet/AAR/ConfigPage/'
		os.chdir(path)
		cmd="git pull"
		os.system(cmd)
		flash ('Update Completed')
	except:
		flash("Error Software Updation")
	return redirect(url_for('mainPage'))

@app.route('/reboot', methods=['POST'])
def reboot():
    
    cmd="reboot"
    os.system(cmd)
    
    return redirect(url_for('mainPage'))

@app.route('/LEDTest', methods=['POST'])
def LEDTest():
	try:
		cmd="/home/pi/Oceannet/AAR/ConfigPage/LEDtest.py"
		os.system(cmd)
		flash ('LED Test Completed')
	except:
		flash("Error Testing Notification LED")
	return redirect(url_for('mainPage'))

app.run(production,debug=False,host="0.0.0.0",port="1000")
