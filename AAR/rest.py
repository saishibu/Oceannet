#!/usr/bin/python

from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()
urls=("/favicon.ico","dummy")
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'amma'
app.config['MYSQL_DATABASE_DB'] = 'Oceannet'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/bs1')
def bs1():
	cur = mysql.connect().cursor()
	cur.execute('select * from basestation where bs=100  ORDER BY id DESC LIMIT 1 ')
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
	return jsonify({'Recent data from Base station 1' : r})

@app.route('/bs2')
def bs2():
        cur = mysql.connect().cursor()
        cur.execute('select * from basestation where bs=66  ORDER BY id DESC LIMIT 1 ')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Recent data from Base Station 2' : r})

@app.route('/dev')
def dev():
        cur = mysql.connect().cursor()
        cur.execute('select * from basestation where devices>0')
        r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
        return jsonify({'Last connected device' : r})



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=1)

