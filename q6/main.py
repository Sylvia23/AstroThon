# all imports below
import math

def sin(x): return math.sin(math.radians(x))
def cos(x): return math.cos(math.radians(x))

g = 9.81
h =  8848
re = 6371000
lat1 = 27.9881
lon1 = 86.9250

def findstrike(velocity: float, alt: float, az: float):
   	
	u = velocity
	r1 = ((u**2)*(sin(2*az)))/g
	r2 = ((u*cos(az))/g)
	r2_= math.sqrt(((u*sin(az))**2) + (2*g*h)) - (u*sin(az))
	r2 = r2*r2_
	r = r1+r2
	b = r/re

	a = math.degrees(math.acos(	cos(b)*cos(90-lat1) + (sin(90-lat1)*sin(b)*cos(az))	))
	B = math.degrees(math.asin(	(sin(b)*sin(az))/sin(a)	))
	lat2 = round(90-a,5)
	lon2 = round(lon1+B,5)

	return tuple([lat2,lon2])

print(findstrike(float(input()), float(input()), float(input())))

# print(findstrike(10,40,0))
