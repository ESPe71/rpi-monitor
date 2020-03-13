# RPi-Monitor

Monitoring an Raspberry Pi with an OLED

## Requirements

Make sure the I2C-Interface is activated.  
You can use the tool ``raspi-config``-->``Interface Options``-->``I2C``.

You need following installations:

- ``sudo apt-get install i2c-tools``
- ``sudo apt-get install python3-pip``
- ``sudo pip3 install adafruit-circuitpython-ssd1306``
- ``sudo apt-get install python3-pil``
- ``sudo apt-get install ttf-dejavu``

You can determine the address of the i2c wire interface with the following command:  
``i2cdetect -y 1``

### Wiring the OLED to the Rasperry Pi

OLED  Pi
Gnd   Gnd
VCC   3.3V
SDA   SDA (Pin 3)
SCL   SCL (Pin 5)

## Setup

In file ``stats.py`` check what information you want to display.

You can it run locally with:  
``./stats.py`` or  
``phyton3 stats.py``


## Start at system startup

Add in ``/etc/rc.local`` the following line:

```
sudo python3 /home/pi/rpi-monitor/stats.py &
```


