
import display

import time
from datetime import datetime, timedelta

import json
import requests

def drawEntries(y):
  try:
    response = requests.get("http://192.168.1.25/admin/api.php?summary")
    j = json.loads(response.text)
  
    pt = j["ads_percentage_today"]
    idx = pt.find(".")
    if idx < 0:
      idx = len(pt)
    pt = " (" + pt[:idx] + "%)"
  except:
    j = {
          "unique_clients" : "---",
          "dns_queries_today" : "---",
          "ads_blocked_today" : "---",
          "unique_domains" : "---",
          "domains_being_blocked" : "---",
        }
    pt = ""

  display.drawEntries(("clients: " + j["unique_clients"],
                    "queries: " + j["dns_queries_today"],
                    "blocked: " + j["ads_blocked_today"] + pt,
                    "domains: " + j["unique_domains"],
                    "blocklist: " + j["domains_being_blocked"]),
                    y, 12, 2)
  return

def drawPage(duration):
  now = datetime.now()
  duration = timedelta(seconds=duration)
  while (datetime.now() - now).seconds < duration.seconds:
    display.clear()
    y = display.drawHeader(15, "Pi-Hole")
    drawEntries(y)
    display.show()
  return
