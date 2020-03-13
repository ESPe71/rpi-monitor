
import display

import time
from datetime import datetime, timedelta

import subprocess

def getSubProcess(cmd):
  return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True).communicate()[0].decode("utf-8")
def getIP():
  cmd = "hostname -I | cut -d\' \' -f1"
  return getSubProcess(cmd)
def getCpuLoad():
  cmd = "top -bn1 | grep \"%Cpu(s):\" | awk '{printf \"CPU: %.0f%%\", 100 - $(NF-9)}'"
  return getSubProcess(cmd)
def getMemUsage():
  cmd = "free -m | awk 'NR==2{printf \"Mem: %.0f%%\", $3*100/$2 }'"
  return getSubProcess(cmd)
def getDiskUsage():
  cmd = "df -h | awk '$NF==\"/\"{printf \"Disk: %s\", $5}'"
  return getSubProcess(cmd)
def getCpuTemp():
  cmd = "vcgencmd measure_temp | cut -c6,7,8,9 | awk '{printf \"Temp: %.0f°C\", $1}'"
  return getSubProcess(cmd)


def drawPage(duration):
  now = datetime.now()
  duration = timedelta(seconds=duration)
  while (datetime.now() - now).seconds < duration.seconds:
    display.clear()
    y = display.drawHeader(15, getIP())
    display.drawEntries((getCpuLoad(), getMemUsage(), getDiskUsage(), getCpuTemp()), y, 12, 2)
    display.show()
    time.sleep(0.250)
  return
