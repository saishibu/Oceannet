#!/usr/bin/python
import subprocess,datetime,pymysql,sys,time,psutil
from time import mktime

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
    RAM = psutil.virtual_memory()
    RAM=RAM[1]/(1024*1024)
    print(RAM)

    print("CPU usage in %")
    CPU=psutil.cpu_percent(interval=None)
    CPU=float(CPU)
    CPUFreq=psutil.cpu_freq()
    CPUCurrent=CPUFreq[0]
    CPUMin=CPUFreq[1]
    CPUMax=CPUFreq[2]
    
    disk=psutil.disk_usage('/')
    disk=disk[2]/(1024*1024)
  
    data={'time':unix_secs,'temp':temp,'CPU':CPU,'RAM':RAM,'disk':disk,'CPUCurrent':CPUCurrent,'CPUMin':CPUMin,'CPUMax':CPUMax}
    cur.execute("INSERT INTO performance (timestamp,temp,RAM,CPU,disk,CPUCurrent,CPUMax,CPUMin) VALUES (%(time)s,%(temp)s,%(RAM)s,%(CPU)s,%(disk)s,%(CPUCurrent)s,%(CPUMin)s,%(CPUMax)s);",data)
    conn.commit()
    print("Committed")
    time.sleep(120)

except KeyboardInterrupt:
  conn.close()
  sys.exit()
