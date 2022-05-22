"""
dbIoTspmatrix MQTT message processing wokwi demo

To view the data:
1. Go to http://www.hivemq.com/demos/websocket-client/
2. Click "Connect"
3. Under Subscriptions, click "Add New Topic Subscription"
4. In the Topic field, type "dIoTspmatrix-data" then click "Subscribe"
5. In the Topic field, type "dIoTspmatrix-cmd" then click "Subscribe"
"""

from MatrixSparseDOK import *

import machine
import network
import time
import ujson
from uuid import *
from umqtt.simple import MQTTClient


# MQTT Server Parameters
id = machine.unique_id()
print("ID: ",id)
print("ID0: ",id[0])
print("ID1: ",id[1])
print("ID2: ",id[2])
print("ID3: ",id[3])

# MQTT_CLIENT_ID  = '{:02x}{:02x}{:02x}{:02x}'.format(id[0], id[1], id[2], id[3])
MQTT_CLIENT_ID  = "User1"
MQTT_BROKER     = "broker.mqttdashboard.com"
MQTT_USER       = "USER2"
MQTT_PASSWORD   = "USER2"
MQTT_TOPIC_DATA = "dIoTspmatrix-data"
MQTT_TOPIC_CMD  = "dIoTspmatrix-cmd"
MQTT_TOPIC_NET  = "dIoTspmatrix-net"

# Connect to WiFi
print("Connecting to WiFi", end="")
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Wokwi-GUEST', '')
while not sta_if.isconnected():
  print(".", end="")
  time.sleep(0.1)
print(" Connected!")

# Connect to MQTT server
print("Connecting to MQTT server... ", end="")
client = MQTTClient("so para testar", MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
client.connect()
print("Connected!")

cmd_messages = list()
data_messages = list()

def mqtt_callback(topic, message):
    global cmd_messages
    print("Message recebida: ",message)
    print()
    cmd_msg = ujson.loads(message)
    try:
        if cmd_msg["node_to"] == MQTT_CLIENT_ID or cmd_msg["node_to"] == "ANY":
            print("Mensagem para mim")
            cmd_messages.append(cmd_msg)
    except:
        print("Mensagem recebida não mal formatada")

client.set_callback(mqtt_callback)
client.subscribe(MQTT_TOPIC_CMD)

m1 = MatrixSparseDOK()
m1_data = {(5, 5): 5.5, (5, 6): 5.6, (6, 7): 6.7, (7, 4): 7.4, (7, 5): 7.5, (7, 8): 7.8}
for key, value in m1_data.items():
    m1[Position(key[0], key[1])] = value
vc = m1.compress()
vc = [[5, 4], 0.0, [7.4, 7.5, 5.5, 5.6, 7.8, 6.7, 0.0], [7, 7, 5, 5, 7, 6, -1], [1, 2, 0]]

def process_commands():
    global cmd_messages
    t = time.localtime()
    for i in range(len(cmd_messages)):
        cmd_msg = cmd_messages[0]
        print(cmd_msg)
        if cmd_msg["cmd"] == "GET-NODE-LOG-FULL":
            message = ujson.dumps({
                "cmd": "GET-NODE-LOG-FULL",
                "data": vc,
                "log_time": "{:d}:{:02d}".format(t[3], t[4]),
                "node_from": MQTT_CLIENT_ID,
                "node_to": cmd_msg["node_from"],
                "msg_id": cmd_msg["msg_id"]
            })
            print("Message a ser enviada: ", message)
            client.publish(MQTT_TOPIC_DATA, message)
        if cmd_msg["cmd"] == "GET-NODE-LOG-BY-HOUR":
            message = ujson.dumps({
                "cmd": "GET-NODE-LOG-BY-HOUR",
                "data": vc,
                "log_time": "{:d}:{:02d}".format(t[3], t[4]),
                "node_from": MQTT_CLIENT_ID,
                "node_to": cmd_msg["node_from"],
                "msg_id": cmd_msg["msg_id"]
            })
            print("Message a ser enviada: ", message)
            client.publish(MQTT_TOPIC_DATA, message)
        if cmd_msg["cmd"] == "GET-NODE-LOG-BY-MINUTE":
            message = ujson.dumps({
                "cmd": "GET-NODE-LOG-BY-MINUTE",
                "data": vc,
                "log_time": "{:d}:{:02d}".format(t[3], t[4]),
                "node_from": MQTT_CLIENT_ID,
                "node_to": cmd_msg["node_from"],
                "msg_id": cmd_msg["msg_id"]
            })
            print("Message a ser enviada: ", message)
            client.publish(MQTT_TOPIC_DATA, message)
        if cmd_msg["cmd"] == "GET-LOG-FULL-EDGE":
            message = ujson.dumps({
                "cmd": "GET-LOG-FULL-EDGE",
                "data": vc,
                "log_time": "{:d}:{:02d}".format(t[3], t[4]),
                "node_from": MQTT_CLIENT_ID,
                "node_to": cmd_msg["node_from"],
                "msg_id": cmd_msg["msg_id"]
            })
            print("Message a ser enviada: ", message)
            client.publish(MQTT_TOPIC_DATA, message)
        cmd_messages.pop(0)

def full_log(day,to):
    message = ujson.dumps({
    "cmd": "GET-NODE-LOG-FULL",
    "day":day,
    "node_from": MQTT_CLIENT_ID,
    "node_to": to,
    "msg_id": str(uuid4())
})
    print("A enviar: ", message)
    client.publish(MQTT_TOPIC_CMD, message)

def by_hour_log(day,hour,to):
    message = ujson.dumps({
    "cmd": "GET-NODE-LOG-BY-HOUR",
    "day":day,
    "hour":hour,
    "node_from": MQTT_CLIENT_ID,
    "node_to": to,
    "msg_id": str(uuid4())
})
    print("A enviar: ", message)
    client.publish(MQTT_TOPIC_CMD, message)


def by_minute_log(day,minute,to):
    message = ujson.dumps({
    "cmd": "GET-NODE-LOG-BY-MINUTE",
    "day":day,
    "minute": minute,
    "node_from": MQTT_CLIENT_ID,
    "node_to": to,
    "msg_id": str(uuid4())
})
    print("A enviar: ", message)
    client.publish(MQTT_TOPIC_CMD, message)

def full_edge_log(day,to):
    message = ujson.dumps({
    "cmd": "GET-LOG-FULL-EDGE",
    "day":day,
    "node_from": MQTT_CLIENT_ID,
    "node_to": to,
    "msg_id": str(uuid4())
})
    print("A enviar: ", message)
    client.publish(MQTT_TOPIC_CMD, message)
    


full_log(0,"User2")
by_minute_log(0,23,"User2")
by_hour_log(0,13,"User2")
full_edge_log(0,"User2")

while (True):
    client.check_msg()
    process_commands()
    time.sleep(1)
