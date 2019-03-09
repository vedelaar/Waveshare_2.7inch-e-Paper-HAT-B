#!/usr/bin/python
# -*- coding:utf-8 -*-

import epd2in7b
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
import random

epd = epd2in7b.EPD()
try:
    epd.init()
    # Drawing on the Horizontal image
    #HBlackimage = Image.new('1', (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)  # 298*126
    #HRedimage = Image.new('1', (epd2in7b.EPD_HEIGHT, epd2in7b.EPD_WIDTH), 255)  # 298*126    
    
    #HBlackimage = Image.open('2in7b-b.bmp')
    #HRedimage = Image.open('2in7b-r.bmp')
    #epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
    

    #HBlackimage = Image.new('1', (24, 24), 255)  # 24*24
    #HRedimage = Image.new('1', (24, 24), 255)  # 24*24    
    #HBlackimage = Image.open('zwart.bmp')
    #HRedimage = Image.open('rood.bmp')
    #epd.displayPartial(epd.getbuffer(HBlackimage, 24, 24), epd.getbuffer(HRedimage, 24, 24),32,32,24,24)
    
    #epd.getTemp()
    #epd.getLowPower()
    
    
    for i in range(1,40,2):
        HBlackimage = Image.new('1', (176, 2), 255)
        HRedimage = Image.new('1', (176, 2), 255)
        draw = ImageDraw.Draw(HBlackimage)
        draw.line([(0, 0), (176, 0)], fill=255)
        draw.line([(0, 1), (176, 1)], fill=255)
        ran = random.randint(0, 176)
        draw.line([(ran, 0), (176, 0)], fill=0)
        draw.line([(ran, 1), (176, 1)], fill=0)
        red=0
        if random.randint(0, 1) == 1:
            red=1
            HRedimage = HBlackimage 
        #draw.line([(0, 1), (176, 1)], fill=0)
        #HBlackimage.save("/home/pi/screen/RaspberryPi/python3/img.png", "PNG")
        print("going for i: "+str(i)+" with red="+str(red)+" with rand="+str(ran))
        epd.displayPartial(epd.getbuffer(HBlackimage, 176, 2), epd.getbuffer(HRedimage, 176, 2),0,i,176,2)
    
    epd.sleep()
        
except :
    print ('traceback.format_exc():\n%s',traceback.format_exc())
    epd.sleep()
    exit()
