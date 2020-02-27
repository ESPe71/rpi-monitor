import display
import net

import time
from datetime import datetime, timedelta

import requests
import xml.etree.ElementTree as xml

ccuIP = ""

def getCCU():
  global ccuIP
  if len(ccuIP) < 7:
    ccuIP = net.getIP("ccu.penetti.de")
  return ccuIP
def resetCCU():
  global ccuIP
  ccuIP = ""
  return
def drawEntries(y):
  dc = "---";
  a = 0;
  try:
    response = requests.get("http://" + getCCU() + "/config/xmlapi/sysvarlist.cgi")
    root = xml.fromstring(response.text)
    for element in root.findall("systemVariable"):
      n = element.get("name")
      v = element.get("value")
      if n == "DutyCycle":
        dc = v
      elif "Alarm" in n:
        if "true" == v:
          a += 1
  except:
    a = "---"
    resetCCU()
  s = 0
  try:
    response = requests.get("http://" + getCCU() + "/config/xmlapi/systemNotification.cgi")
    root = xml.fromstring(response.text)
    for element in root.findall("notification"):
      s += 1
  except:
    s = "---"
    resetCCU()

  if dc == "---":
    dc = "DC: ---"
  else:
    dc = "DC: {0:.0f}%".format(float(dc))
  if s == "---":
    s = "Service: ---"
  else:
    s = "Service: {0:d}".format(s)
  if a == "---":
    a = "Alarm: ---"
  else:
    a = "Alarm: {0:d}".format(a)

  display.drawEntries(("IP: " + getCCU(), a, s, dc), y, 12, 2)
  return

def drawPage(duration):
  now = datetime.now()
  duration = timedelta(seconds=duration)
  while (datetime.now() - now).seconds < duration.seconds:
    display.clear()
    y = display.drawHeader(15, "CCU")
    drawEntries(y)
    display.show()
  return
