# all imports below

def findDelay(dist):
	me=5.974e24
	c=2.998e8
	G=6.674e-11
	re=6357000

	h=dist

	v=((G*me)/(re+h))**0.5								#velocity of satellite

	T=h/c

	sg=1-((1-(2*G*me)/(re*c**2))/(1-(2*G*me)/((re+h)*c**2)))**0.5			#Schwarzchild gain
	lv=1/(1-(v/c)**2)**0.5-1							#Loss due to velocity

	delta_t=sg-lv

	print(delta_t*T*10**9)
	#time gained in nanoseconds in a duration of time T

if __name__=="__main__":
	dist=float(input())
	findDelay(dist)
