import subprocess,datetime
OTA=subprocess.call(['sudo','git','pull'])
print "OTA Updation success at "+str(datetime.datetime.now())
