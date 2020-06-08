import ephem
from datetime import datetime, timedelta
from math import degrees

"""
Any extra lines of code (if required)
as helper for this function.
"""

startobs = datetime(2020, 6, 9, 0, 9, 6)
endobs = datetime(2020, 6, 9, 6, 41, 41)


def findSaturn(obstime):
    """
	Parameters
	----------
	obstime : A `~datetime.datetime` instance.
	
	Returns
	-------
	A `tuple` of two floats.
	"""
    obstime = obstime - timedelta(0, 0, 0, 0, 30, 5)
    obs = ephem.Observer()
    obs.lon, obs.lat = "76.993694", "31.781476"
    obs.elevation = 1000
    obs.date = f"{obstime.year}/{obstime.month}/{obstime.day} {obstime.hour}:{obstime.minute}:{obstime.second}"
    sat = ephem.Saturn()
    sat.compute(obs)
    alt = degrees(float(repr(sat.alt)))
    az = degrees(float(repr(sat.az)))
    return alt, az

