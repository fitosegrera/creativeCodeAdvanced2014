#!/usr/bin/python
# -*- coding: utf-8 -*-

# pyduino - Library to communicate with the arduino YUN via serialport
# Created by: fito_segrera 
# www.fii.to
# 10-1-14

from time import sleep
import serial

class Pyduino:
	def connect(self):
		ser = serial.Serial('/dev/ttyATH0', 9600) #Establish the connection on a speci

	def digitalWrite(self, state):
		while True:
			ser.write(chr(state))
			sleep(1)
