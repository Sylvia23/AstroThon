# all imports below
import math

g = 9.81
h = 8848
re = 6371000
lat1 = 27.9881
lon1 = 86.9250

def findstrike(velocity: float, alt: float, az: float):
   	
	u = velocity
	alt = math.radians(alt)
	az = math.radians(az)
	r1 = ((u**2)*(math.sin(2*az)))/g
	r2 = ((u*math.cos(az))/g)
	r2_= math.sqrt(((u*math.sin(az))**2) + (2*g*h)) - (u*math.sin(az))
	r2 = r2*r2_
	r = r1+r2
	b = r/re

	a = math.acos(	math.cos(b)*math.cos(90-lat1) + (math.sin(90-lat1)*math.sin(b)*math.cos(az))	)
	B = math.asin(	(math.sin(b)*math.sin(az))/math.sin(a)	)
	lat2 = round(90-a,5)
	lon2 = round(lon1+B,5)

	return tuple([lat2,lon2])

print(findstrike(float(input()), float(input()), float(input())))
