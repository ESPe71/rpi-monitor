import display

import time
from datetime import datetime

def drawPage(header, entries, duration):
  now = datetime.now()
  display.clear()
  y = display.drawHeader(20, header)
  display.drawEntries(entries, y, 15, 1)
  display.show()
  time.sleep(duration - (datetime.now() - now).seconds)
  return
