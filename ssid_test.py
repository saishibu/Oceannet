#test script
import nanostation as ns
ssid=ns.extssid()
print ssid
cpe_ip=ns.mapip(ssid)
print cpe_ip
