
import display
from PIL import Image

import time
from datetime import datetime, timedelta

import subprocess

def getSubProcess(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True).communicate()[0].decode("utf-8")
def getAkku():
  cmd = "upsc ups@localhost | grep battery.charge: | awk '{printf \"Akku: %.0f%%\", $2}'"
  return getSubProcess(cmd)
def getRuntime():
  cmd = "upsc ups@localhost | grep battery.runtime: | awk '{printf \"Laufzeit: %.0fs\", $2}'"
  return getSubProcess(cmd)
def getInput():
  cmd = "upsc ups@localhost | grep input.voltage: | awk '{printf \"%.0fV\", $2}'"
  return getSubProcess(cmd)
def getOutput():
  cmd = "upsc ups@localhost | grep output.voltage: | awk '{printf \"%.0fV\", $2}'"
  return getSubProcess(cmd)
def getVoltage():
  return "U: " + getInput() + " / " + getOutput()
def getLoad():
  cmd = "upsc ups@localhost | grep ups.load: | awk '{printf \"Auslastung: %.0f%%\", $2}'"
  return getSubProcess(cmd)

def drawPage(duration):
  now = datetime.now()
  duration = timedelta(seconds=duration)
  while (datetime.now() - now).seconds < duration.seconds:
    display.clear()
    y = display.drawHeader(15, "USV")
    display.drawEntries((getAkku(), getRuntime(), getVoltage(), getLoad()), y, 12, 2)
#    display.DRAW.bitmap((0,0), Image.open('ac.png').convert("RGBA"))
    display.show()
  return
