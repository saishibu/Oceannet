#!/usr/bin/python3
from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os,pymysql, getOTP, time

# import RPi.GPIO as GPIO
# GPIO.setmode(GPIO.BCM) 
# GPIO.setwarnings(False) 
# GPIO.setup(17,GPIO.OUT)  #REV
# GPIO.setup(27,GPIO.OUT)  #FWD
# GPIO.setup(26,GPIO.OUT)  #Status LED
# GPIO.setup(19,GPIO.OUT) #RSSI 0
# GPIO.setup(13,GPIO.OUT)	#RSSI 1
# GPIO.setup(6,GPIO.OUT)  #RSSI 2
# GPIO.setup(5,GPIO.OUT)  #RSSI 3

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
    username=""
    password=""
    
    try:
        conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
        cur=conn.cursor()
        cur.execute("SELECT username,password FROM register;")
        data=cur.fetchone()
        username=data[0]
        password=data[1]
         
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
    except:
        flash("User not registered")
        username=""
        password=""
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
        return home()
    except:
        flash('Error Saving Configurations')
        return home()


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

@app.route('/AARTestfwd', methods=['POST'])
def AARTestfwd():
    try:
        cmd="/home/pi/Oceannet/AAR/ConfigPage/Rotatetest.py"
        os.system(cmd)
        flash ('AAR Test Completed')
    except:
        flash("Error Testing")
	return redirect(url_for('mainPage'))

# @app.route('/AARTestrev', methods=['POST'])
# def AARTestrev():
# 	try:
# 		GPIO.setup(17,GPIO.HIGH)
# 		time.sleep(10)#FWD
# 		GPIO.setup(17,GPIO.LOW)
# 		flash ('AAR Test Completed')
# 	except:
# 		flash("Error Testing")
# 	return redirect(url_for('mainPage'))

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

@app.route('/LEDTest1', methods=['POST'])#status
def LEDTest1():
	try:
        cmd="/home/pi/Oceannet/AAR/ConfigPage/LEDtest.py"
        os.system(cmd)


		# GPIO.setup(26,GPIO.HIGH)
		# time.sleep(2)#FWD
		# GPIO.setup(26,GPIO.LOW)
		flash ('LED Test Completed')
	except:
		flash("Error Testing Notification LED")
	return redirect(url_for('mainPage'))

# app.route('/LEDTest2', methods=['POST'])#rssi1
# def LEDTest2():
# 	try:
# 		GPIO.setup(19,GPIO.HIGH)
# 		time.sleep(2)#FWD
# 		GPIO.setup(19,GPIO.LOW)
# 		flash ('RSSI1 Test Completed')
# 	except:
# 		flash("Error Testing Notification LED")
# 	return redirect(url_for('mainPage'))
# @app.route('/LEDTest3', methods=['POST'])#rssi2
# def LEDTest3():
# 	try:
# 		GPIO.setup(13,GPIO.HIGH)
# 		time.sleep(2)#FWD
# 		GPIO.setup(13,GPIO.LOW)
# 		flash ('RSSI2 Test Completed')
# 	except:
# 		flash("Error Testing Notification LED")
# 	return redirect(url_for('mainPage'))
# @app.route('/LEDTest4', methods=['POST'])#rssi3
# def LEDTest4():
# 	try:
# 		GPIO.setup(6,GPIO.HIGH)
# 		time.sleep(2)#FWD
# 		GPIO.setup(6,GPIO.LOW)
# 		flash ('RSSI3 Test Completed')
# 	except:
# 		flash("Error Testing Notification LED")
# 	return redirect(url_for('mainPage'))
# @app.route('/LEDTest5', methods=['POST'])#rssi4
# def LEDTest5():
# # 	try:
# 	GPIO.setup(5,GPIO.HIGH)
# 	time.sleep(2)#FWD
# 	GPIO.setup(5,GPIO.LOW)
# 	flash ('RSSI1 Test Completed')
# 	except:
# 		flash("Error Testing Notification LED")
	return redirect(url_for('mainPage'))

app.run(debug=False,host="0.0.0.0",port="1000")
