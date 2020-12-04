# RPi-Monitor

Monitoring an Raspberry Pi with an OLED

You can buy an OLED for example on [Amazon](https://amzn.to/2MeAtls).
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


|OLED | Pi
|-----|-----------
|Gnd  | Gnd  
|VCC  | 3.3V  
|SDA  | SDA (Pin 3)  
|SCL  | SCL (Pin 5)  


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

## Using another I2C-Bus as Bus 1 on Raspberry Pi 4

First have a look in /boot/overlays/README. Here you can look for Name i2c1, i2c2, i2c3, i2c4, i2c5 or i2c6.

In the ``/boot/config.txt`` add an entry for your choosen i2c-Bus.

```
#Name:   i2c4
#Info:   Enable the i2c4 bus. BCM2711 only.
#Load:   dtoverlay=i2c4,<param>
#Params: pins_6_7                Use GPIOs 6 and 7
#        pins_8_9                Use GPIOs 8 and 9 (default)
#        baudrate                Set the baudrate for the interface (default
#                                "100000")
dtoverlay=i2c4,pins_8_9
```
Now wire your display as follows (here e.g. for bus 4):

|OLED | Pi
|-----|-----------
|Gnd  | Gnd
|VCC  | 3.3V
|SDA  | GPIO 8 (Pin 24)
|SCL  | GPIO 9 (Pin 21)

Reboot your pi and test the i2c-bus (e.g. bus 4):
```
i2cdetect -y 4
```

You need to install adafruit-extended-bus
```
sudo pip3 install adafruit-extended-bus
```
In your python-script change the creation of the I2C as follows:

```
import adafruit_ssd1306
from adafruit_extended_bus import ExtendedI2C as i2c

DISPLAY_WIDTH  = 128
DISPLAY_HEIGHT = 64

...
...

I2C            = i2c(4)
DISPLAY        = adafruit_ssd1306.SSD1306_I2C(DISPLAY_WIDTH, DISPLAY_HEIGHT, I2C)
```

## References

- https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage
- https://indibit.de/raspberry-pi-oled-display-128x64-mit-python-ansteuern-i2c/
- https://circuitpython.readthedocs.io/projects/extended_bus/en/latest/
- https://keytosmart.com/single-board-computers/raspberry-pi-4-gpio-pinout/


