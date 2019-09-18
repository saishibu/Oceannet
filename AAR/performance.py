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
    
    disk=psutil.disk_usage('/')
    disk=float(disk[2]/(1024*1024*1024))
    netIO=psutil.net_io_counters()
    
    data={'time':unix_secs,'temp':temp,'CPU':CPU,'RAM':RAM,'disk':disk,'CPUCurrent':CPUCurrent,'CPUMin':CPUMin,'CPUMax':CPUMax,'loadAvg1':loadAvg1,'loadAvg5':loadAvg5,'loadAvg15':loadAvg15,'bytes_sent':netIO[0],'bytes_recv':netIO[1],'packets_sent':netIO[2],'packets_recv':netIO[3],'errin':netIO[4],'errout':netIO[5],'dropin':netIO[6],'dropout':netIO[7]}
    cur.execute("INSERT INTO performance (timestamp,temp,RAM,CPU,disk,CPUFreqCurrent,CPUFreqMax,CPUFreqMin,loadAvg1,loadAvg5,loadAvg15,bytes_sent,bytes_recv,packets_sent,packets_recv,errin,errout,dropin,dropout) VALUES (%(time)s,%(temp)s,%(RAM)s,%(CPU)s,%(disk)s,%(CPUCurrent)s,%(CPUMin)s,%(CPUMax)s,%(loadAvg1)s,%(loadAvg5)s,%(loadAvg15)s,%(bytes_sent)s,%(bytes_recv)s,%(packets_sent)s,%(packets_recv)s,%(errin)s,%(errout)s,%(dropin)s,%(dropout)s);",data)    
    conn.commit()
    print(data)
    print("Committed")
    time.sleep(120)

except KeyboardInterrupt:
  conn.close()
  sys.exit()
