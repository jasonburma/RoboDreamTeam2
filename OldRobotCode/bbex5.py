#!/usr/bin/env python3

#Lab 6


from ev3dev.ev3 import *
from time import sleep
import ev3dev.fonts as fonts
from PIL import Image, ImageDraw, ImageFont

lcd = Screen()

# Connect ultrasonic sensor to any sensor port
# and check it is connected.
us = UltrasonicSensor() 
assert us.connected, "Connect a US sensor to any sensor port"
# Put the US sensor into distance mode.
us.mode='US-DIST-CM'

while us.value()> 80:   # 8 cm converted to mm
    lcd.clear()
    lcd.draw.text((40,50),str(us.value()/10)+' cm', font=fonts.load('helvB24'))
    lcd.update()
    sleep(0.1) # so the display doesn't change too frequently

pic = Image.open('pics/Up.bmp')
lcd.image.paste(pic, (0,0))
lcd.update()

sleep(5)  # when running from Brickman, need time to admire image