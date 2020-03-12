import paho.mqtt.client as mqtt

# This is the Publisher
def helper(data):
  client = mqtt.Client()
  client.connect("103.10.24.222",1883,60)
  client.publish("SGM/onpiggyback",data);
  print("piggyback sent")
  client.disconnect();
