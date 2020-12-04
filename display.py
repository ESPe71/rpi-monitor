import adafruit_ssd1306
from adafruit_extended_bus import ExtendedI2C as i2c

from PIL import Image, ImageDraw, ImageFont

DISPLAY_WIDTH  = 128
DISPLAY_HEIGHT = 64

IMAGE          = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT))
DRAW           = ImageDraw.Draw(IMAGE)
I2C            = i2c(4)
DISPLAY        = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, I2C)

fonts = {}


def show():
  DISPLAY.image(IMAGE)
  DISPLAY.show()
  return
def clear(): 
  DRAW.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0)
  return
clear()
show()

def getFont(fontSize):
  try:
    font = fonts[fontSize]
  except:
    font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', fontSize)
    fonts[fontSize] = font
  return font

def drawHeader(fontSize, header):
  font = getFont(fontSize)
  size = font.getsize(header)
  if size[0] > DISPLAY_WIDTH:
    r = float(DISPLAY_WIDTH / size[0])
    font = getFont(int(fontSize * r))
    size = font.getsize(header)
   
  DRAW.text(((DISPLAY_WIDTH - size[0]) / 2, 0), header, font=font, fill=255)
  DRAW.line((0, size[1] + 2, DISPLAY_WIDTH, size[1] + 2), fill=1)
  return size[1] + 4

def HAlign(maxWidth, txtWidth, align):
  x = 0
  switcher = {
        1: (maxWidth - txtWidth) / 2, # center
        2: 0,                         # left
        3: maxWidth - txtWidth,       # right
    }
  return switcher.get(align, 0)
def drawEntries(entries, y, maxFontSize, alignment):
  try:
    entries.isalpha()
    length = 1
  except:
    length = len(entries)
  fontSize = int((DISPLAY_HEIGHT - y) / length)
  if fontSize > maxFontSize:
    fontSize = maxFontSize
  font = getFont(fontSize)
  y = y + ((DISPLAY_HEIGHT - y - length * fontSize) / 2)
  if length == 1:
    size = font.getsize(entries)
    DRAW.text((HAlign(DISPLAY_WIDTH, size[0], alignment), y), entries, font=font, fill=255)
  else:
    for entry in entries:
      size = font.getsize(entry)
      DRAW.text((HAlign(DISPLAY_WIDTH, size[0], alignment), y), entry, font=font, fill=255)
      y += fontSize
  return
  
