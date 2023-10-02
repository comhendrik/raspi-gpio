import time
import sys
from luma.core.interface.serial import spi
from luma.lcd.device import st7735
from luma.core.render import canvas

s = spi(port=0, device=0, gpio_DC=23, gpio_RST=24)
device=st7735(s)

import RPi.GPIO as GPIO

GPIO.setwarnings(False)

gpio_LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_LED, GPIO.OUT, initial=0)

GPIO.output(gpio_LED, 1)
counter = 0
while True:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline='blue', fill=(22, 55, 55))
        draw.text((50, 50), str(counter), fill='red')
        counter += 1
    time.sleep(1)
        
            