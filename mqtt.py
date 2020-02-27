import paho.mqtt.client as mqtt

import time
from datetime import datetime, timedelta

import display

MQTT = mqtt.Client()

CLIENTS_ACTIVE = "$SYS/broker/clients/connected"
MESSAGES_DROPPED = "$SYS/broker/publish/messages/dropped"
MESSAGES_RECEIVED = "$SYS/broker/publish/messages/received"
MESSAGES_SENT = "$SYS/broker/publish/messages/sent"
SUBSCRIPTIONS = "$SYS/broker/subscriptions/count"

clientsActive = "---"
msgDropped = "0"
msgReceived = "---"
msgSent = "---"
subscriptions = "---"

def onMessage(client, obj, msg):
  global clientsActive, msgDropped, msgReceived, msgSent, subscriptions
  #print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
  if msg.topic == CLIENTS_ACTIVE:
    clientsActive = msg.payload.decode("utf-8")
  elif msg.topic == MESSAGES_DROPPED:
    msgDropped = msg.payload.decode("utf-8")
  elif msg.topic == MESSAGES_RECEIVED:
    msgReceived = msg.payload.decode("utf-8")
  elif msg.topic == MESSAGES_SENT:
    msgSent = msg.payload.decode("utf-8")
  elif msg.topic == SUBSCRIPTIONS:
    subscriptions = msg.payload.decode("utf-8")
    

MQTT.on_message = onMessage
MQTT.connect("mqtt.penetti.de", 1883)

MQTT.subscribe(CLIENTS_ACTIVE, 0)
MQTT.subscribe(MESSAGES_DROPPED, 0)
MQTT.subscribe(MESSAGES_RECEIVED, 0)
MQTT.subscribe(MESSAGES_SENT, 0)
MQTT.subscribe(SUBSCRIPTIONS, 0)

def drawEntries(y):
  if clientsActive == "---":
    ca = "Teilnehmer: ---"
  else:
    ca = "Teilnehmer: {0:,d}".format(int(clientsActive))
  if msgDropped != "0":
      md = "Verworfen: {0:,d}".format(int(msgDropped))
  if msgReceived == "---":
    mr = "Empfangen: ---"
  else:
    mr = "Empfangen: {0:,d}".format(int(msgReceived))
  if msgSent == "---":
    ms = "Gesendet: ---"
  else:
    ms = "Gesendet: {0:,d}".format(int(msgSent))
  if subscriptions == "---":
    s = "Abonniert: ---"
  else:
    s = "Abonniert: {0:,d}".format(int(subscriptions))
  if msgDropped != "0":  
    display.drawEntries((ca, md, mr, ms, s), y, 12, 2)
  else:
    display.drawEntries((ca, mr, ms, s), y, 12, 2)
  return
def drawPage(duration):
  now = datetime.now()
  duration = timedelta(seconds=duration)
  MQTT.loop_start()
  while (datetime.now() - now).seconds < duration.seconds:
    display.clear()
    y = display.drawHeader(15, "Mosquitto")
    drawEntries(y)
    display.show()
    time.sleep(.1)
  MQTT.loop_stop()
  return
  
#MQTT.subscribe("$SYS/#")
#MQTT.loop_start()
#time.sleep(15)
#MQTT.loop_stop
