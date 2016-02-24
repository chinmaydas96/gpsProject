#!/usr/bin/env python

#from geopy.geocoders import Nominatim
#from geopy.exc import GeocoderTimedOut
import serial
import time 
import asyncio
import websockets

ser =serial.Serial("/dev/tty.usbmodem1421", 9600, timeout=1)

async def hello():
	async with websockets.connect('ws://localhost:8765') as websocket:
		while True:
			data = await retrieve()
			await websocket.send(data)
			print("> {}".format(data))
			greeting = await websocket.recv()
			print("< {}".format(data))


async def retrieve():
		data = ser.readline()
		return data #return the location from your example

			#for line in data.split('\n') :
				#if line.startswith( '$GPGGA' ) :           # latitude and longitude data find in GPGGA format                   
						#lat, _, lon = line.strip().split(',')[2:5]     
					#lat_toF = float( lat )
					#lon_toF = float( lon )
					#N_lat =str(lat_toF/100)
					#N_lon =str(lon_toF/100)             # converting from float to string

					#e=int (float(N_lat[3:])*100/60)     # for converting from degree to decimal
					#LAT=N_lat[:3]+str(e)                # (latitude)
					
					#f=int (float(N_lon[3:])*100/60)     #    ||
					#LON=N_lon[:3]+str(f)                # (longitude)

					#coordinate = LAT + ', ' + LON       # cordinate in string format
					#geolocator = Nominatim()
					#try:
						#location = geolocator.reverse(coordinate,timeout=10)
						#print("LAT  "+ str(location.latitude) + "   LON  " +str( location.longitude))
							#print(location.address)
							#except GeocoderTimedOut as e:
								#print("Error: geocode failed on input %s with message %s"%(my_address, e.msg))




asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()
