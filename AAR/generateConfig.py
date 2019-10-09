#!/usr/bin/python
import pymysql

boatName=raw_input("Enter Boat Name: ")
cpeIP=raw_input("Enter CPE IP: ")

data={"boatName":boatName,"cpeIP":cpeIP}
print("Validate the configurations")
print(data)
ans=raw_input("Store Data (Y/N): ")
if ans == "Y":
  conn =pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
	cur=conn.cursor()
	cur.execute("INSERT INTO boat_data (boatName, cpeIP) VALUES (%(boatName)s, %(cpeIP)S);",data)
	print("Success")
elif ans == "N":
  print("Config Ignored")
else:
  print("Enter Y or N")
  exit()
