# RPi-Monitor

Monitoring an Raspberry Pi with an OLED


## Start at system startup

Add in ``/etc/rc.local`` the following line:

```
sudo python3 /home/pi/rpi-monitor/stats.py &
```


