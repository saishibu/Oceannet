# Oceannet

### Disclaimer: DO NOT COPY WITHOUT PERMISSION
#### Deployment code for Oceannet Automatic Antenna orientation system
Folder has both server(Base Station) and client (Nano Station) apps
Add iperf and automate services

1) Move iperf.service & automate.service to /etc/systemd/system/
2) Enable both the services by systemctl enable iperf.service & systemctl enable automate.service
3)reboot the pi
4) test iperf from base station with port 5001
###### © Amrita Vishwa Vidyapeetham |Amrita Center for Wireless Networks & Applications
####### refer oceannnet.amrita.edu for more details
