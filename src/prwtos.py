import paho.mqtt.client as mqtt
import json


import paho.mqtt.client as mqtt #import the client1 
import time 
############ 
def on_message(client, userdata, message): 
    print("message received " ,str(message.payload.decode("utf-8"))) 
    print("message topic=",message.topic) 
    print("message qos=",message.qos) 
    print("message retain flag=",message.retain) 
######################################## 
broker_address="localhost" 
#broker_address="iot.eclipse.org" 
print("creating new instance") 
client = mqtt.Client("P1") #create new instance 
client.on_message=on_message #attach function to callback 
print("connecting to broker") 
client.connect(broker_address) #connect to broker 
client.loop_start() #start the loop 
print("Subscribing to topic","house/bulbs/bulb1") 
client.subscribe("gateway/b827ebfffe99ebfa/rx") 
print("Publishing message to topic","house/bulbs/bulb1") 
client.publish("gateway/b827ebfffe99ebfa/rx","OFF") 
#time.sleep(4) # wait 
#client.loop_stop() #stop the loop 
client.loop_forever() 


encoded_msg = str(message.payload.decode("utf-8"))
msgdict = json.loads(encoded_msg)


{"rxInfo":{"mac":"b827ebfffe99ebfa","timestamp":2581832844,"frequency":868100000,"channel":0,"rfChain":1,"crcStatus":1,"codeRate":"4/5","rssi":-40,"loRaSNR":9,"size":17,"dataRate":{"modulation":"LORA","spreadFactor":12,"bandwidth":125},"board":0,"antenna":0},"phyPayload":"QESufgGAAAABizI7/Kupf6U="}