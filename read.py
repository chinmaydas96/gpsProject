import serial
import pynmea2

from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim

ser = serial.Serial("/dev/tty.usbserial", 9600, timeout=1)

while True:
	data = ser.readline().decode()

	for line in data.split('\n') :
		if line.startswith( '$GPGGA' ) :
			msg = pynmea2.parse(line)
			print(msg)
			lat = msg.latitude
			lng = msg.longitude
			coordinate = str(lat) + ', ' + str(lng)
			geolocator = Nominatim()
			try:
				location = geolocator.reverse(coordinate,timeout=10)
				print(location.address)
			except GeocoderTimedOut as e:
					print(e)
