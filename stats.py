#!/usr/bin/python3

import title
import system
import ccu
import mqtt



while True:
  title.drawPage("SmartHome", ("CCU", "Node-Red", "Mosquitto"), 5)
  system.drawPage(5)
  ccu.drawPage(5)
  mqtt.drawPage(5)
  
  