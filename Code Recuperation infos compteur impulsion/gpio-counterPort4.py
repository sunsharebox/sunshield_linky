#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import signal
import datetime

#verbose = True     # global variable

############################################################################################################
############################################################################################################
i = 0
########## Main Loop
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
counter=0
while True:
    # wait for pin going up
    GPIO.wait_for_edge(4, GPIO.FALLING)
    while i <10 and GPIO.input(4)==False:
        time.sleep(0.001)
        i=i+1
    if i==10:
        counter=counter+ 1
        now = datetime.datetime.now()
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        print(date,"    Compteur:", counter, "Wh")
    GPIO.wait_for_edge(4, GPIO.RISING)
    i=0
############################################################################################################
############################################################################################################



