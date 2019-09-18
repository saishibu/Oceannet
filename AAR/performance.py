#!/usr/bin/python
import subprocess,datetime,pymysql,sys,time,psutil
from time import mktime

conn = pymysql.connect(database="autosys",user="on",password="amma",host="localhost")
cur=conn.cursor()

try:
  while 1:
    t =datetime.datetime.now()
    unix_secs = int(mktime(t.timetuple()))


    try:
      temp=subprocess.check_output("vcgencmd measure_temp | awk 'NR==1 {print $1}'", shell=True)
      temp=float(temp[5:9])
    except:
      temp=int(subprocess.check_output("cat /sys/class/thermal/thermal_zone0/temp", shell=True))
      temp=temp/1000  

    RAM = psutil.virtual_memory()
    RAM=float(RAM[1]/(1024*1024))

    CPU=psutil.cpu_percent(interval=None)
    CPU=float(CPU)
    CPUFreq=psutil.cpu_freq()
    CPUCurrent=CPUFreq[0]
    CPUMin=CPUFreq[1]
    CPUMax=CPUFreq[2]
    loadAvg=psutil.getloadavg()
    loadAvg1=loadAvg[0]
    loadAvg5=loadAvg[1]
    loadAvg15=loadAvg[2]
    print(loadAvg1)
    disk=psutil.disk_usage('/')
    disk=float(disk[2]/(1024*1024*1024))
  
    data={'time':unix_secs,'temp':temp,'CPU':CPU,'RAM':RAM,'disk':disk,'CPUCurrent':CPUCurrent,'CPUMin':CPUMin,'CPUMax':CPUMax}
    cur.execute("INSERT INTO performance (timestamp,temp,RAM,CPU,disk,CPUFreqCurrent,CPUFreqMax,CPUFreqMin) VALUES (%(time)s,%(temp)s,%(RAM)s,%(CPU)s,%(disk)s,%(CPUCurrent)s,%(CPUMin)s,%(CPUMax)s);",data)
    conn.commit()
    print(data)
    print("Committed")
    time.sleep(120)

except KeyboardInterrupt:
  conn.close()
  sys.exit()
