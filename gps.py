from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import serial
import time 
ser =serial.Serial("/dev/ttyUSB1", timeout=1)               # check the usb port no
while True: 
	data = ser.readline()
	for line in data.split('\n') :
		if line.startswith( '$GPGGA' ) :           # latitude and longitude data find in GPGGA format                   
        		lat, _, lon = line.strip().split(',')[2:5]     
			lat_toF = float( lat )
			lon_toF = float( lon )
			N_lat =str(lat_toF/100)
			N_lon =str(lon_toF/100)             # converting from float to string

			e=int (float(N_lat[3:])*100/60)     # for converting from degree to decimal
			LAT=N_lat[:3]+str(e)                # (latitude)
			
			f=int (float(N_lon[3:])*100/60)     #    ||
			LON=N_lon[:3]+str(f)                # (longitude)

			coordinate = LAT + ', ' + LON       # cordinate in string format
			geolocator = Nominatim()
			try:
				location = geolocator.reverse(coordinate,timeout=10)
				print("LAT  "+ str(location.latitude) + "   LON  " +str( location.longitude))
   			       	print(location.address)
	                except GeocoderTimedOut as e:
		               	print("Error: geocode failed on input %s with message %s"%(my_address, e.msg))
                                                                                    
