#!/usr/bin/env python

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import serial
import time 
import asyncio
import websockets
import pynmea2
from pynmea2 import ChecksumError
from pynmea2 import ParseError

ser =serial.Serial("/dev/tty.usbserial", 9600, timeout=1)

async def hello():
	async with websockets.connect('ws://localhost:8765') as websocket:
		while True:
			data = await retrieve()
			await websocket.send(str(data))
			print("> {}".format(data))
			greeting = await websocket.recv()
			print("< {}".format(data))


async def retrieve():
	data = ser.readline().decode()
	data_to_be_sent = await concurrent(data)
	return(data_to_be_sent)

async def concurrent(data):	
	#while True:
	for line in data.split('\n'):
		if line.startswith('$GPGGA'):
			#if pynmea2.ChecksumError(line):
			try:
				msg = pynmea2.parse(line)
				print(msg)
				lat = msg.latitude
				lng = msg.longitude
				print(lat, lng)
				coordinate = str(lat) + ', ' + str(lng)
				print(coordinate)
				geolocator = Nominatim()
				location = geolocator.reverse(coordinate,timeout=10)
				return(location.address)
			except(ChecksumError, ParseError, KeyError) as e:
				print(e)
				
			




asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
