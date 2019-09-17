#!/usr/bin/python
import subprocess,datetime,pymysql,sys

conn = pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
cur=conn.cursor()

try:
  while 1:
    t =datetime.datetime.now()
    unix_secs = int(mktime(t.timetuple()))

    print("Temperature")

    try:
      temp=subprocess.check_output("vcgencmd measure_temp | awk 'NR==1 {print $1}'", shell=True)
      temp=float(temp[5:9])
    except:
      temp=int(subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True))
      temp=temp/1000  
    print(temp)

    print("Available-RAM")
    RAM=int(subprocess.check_output("free | awk 'NR==2 {print $7}'",shell=True))
    RAM=RAM/1024
    print(RAM)

    print("CPU usage in %")
    CPU=(subprocess.check_output("top -n1 | awk '/Cpu\(s\):/ {print $2}'",shell=True))
    print(CPU)
    CPU=float(CPU)

  #print("Disk Usage in %")
#try:
  #disk=subprocess.check_output("df -h --total | awk 'NR==11 {print $5}'",shell=True)
#print(disk)
#	disk=float(disk[:2])
#	print(disk)
#except:
    disk=0

    data={'time':unix_secs,'temp':temp,'CPU':CPU,'RAM':RAM,'disk':disk}
    cur.execute("INSERT INTO performance (timestamp,temp,RAM,CPU,disk) VALUES (%(time)s,%(temp)s,%(RAM)s,%(CPU)s,%(disk)s);",data)
    conn.commit()
    print("Committed")
    time.sleep(120)

except KeyboardInterrupt:
  conn.close()
  sys.exit()
