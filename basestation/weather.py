#!/usr/bin/python3

#Import required libraries
import json,time,pymysql
import sys
from urllib.request import urlopen
conn =pymysql.connect(database="micronet",user="on",password="amma",host="localhost")
cur=conn.cursor()

#url="https://api.darksky.net/forecast/7a029bd49436a180466fbe67165cbf8e/9.092534,76.489965"
url="https://api.darksky.net/forecast/c2576c4bc8dc2eba05e98617c2ebb6c2/9.092534,76.489965"
api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
data= json_api['currently']
data['temperature']=(data['temperature']-32)*5/9
#print(data)
cur.execute("INSERT INTO weather(time,temperature,humidity,summary)VALUES(%(time)s, %(temperature)s,%(humidity)s,%(summary)s);",data)
cur.close()
conn.commit()
conn.close()
print("DB Update completed")
