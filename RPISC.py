#!/usr/bin/python2.7

#Name: rpi_servo_control
#VER: ALFA
#VER NR: 0.1
#LM: 01-02-2014 

import RPi.GPIO as GPIO
import time

def servo_move(direction):
	pin = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.OUT)
	p = GPIO.PWM(pin,50)
	p.start(direction)
	time.sleep(1)
	p.stop()
	GPIO.cleanup()
