from math import sqrt, sin, cos, atan2, pi
from types import IntType

class Point():
	def __init__(self, x, y):
		self.x = x
		self.y = y

def turn(P, Q, R):
	# It checks for the turn that the segment PQ makes with the segment QR
	# if turn(P,Q,R) > 0, then PQ takes a left to toward QR
	# if turn(P,Q,R) < 0, then PQ takes a right to toward QR
	# if turn(P,Q,R) = 0, then PQ is aligned with QR
	return (Q.x - P.x)*(R.y - P.y) - (Q.y - P.y)*(R.x - P.x)

def getEventFromDay(day):
	assert type(day) is IntType, "day is not an integer: %r" % day
	assert day >= 0
	assert day <= 3650
	if (isDayOfTotalAlignment(day)):
		return 'sequia'
	else:
		sun_pos = Point(0.0, 0.0)
		fer_pos = getFerengiPosition(day)
		bet_pos = getBetasoidPosition(day)
		vul_pos = getVulcanPosition(day)
		if (planetsAreAligned(fer_pos, bet_pos, vul_pos)):
			return 'optimo'
		else:
			if (sunInTriangle(sun_pos, fer_pos, bet_pos, vul_pos)):
				return 'lluvia'
			else:
				return 'nada'


def isDayOfTotalAlignment(day):
	# Every 90 days we have a total alignment (all 3 planets are aligned along with the sun)
	return day % 90 == 0


def epsilon():
	# We use an epsilon to take into account possible numerical error
	return 0.000001

def angle(P, Q):
	dy = P.y - Q.y
	dx = P.x - Q.x
	a = (atan2(dy, dx) * (-180.0) / pi)
	if (a < 0):
		a = a + 360.0
	return a

def planetsAreAligned(fer_pos, bet_pos, vul_pos):
	# Return true if the slope of segment (fer_pos, bet_pos) is **similar** to the slope of the segment (bet_pos, vul_pos)
	return abs(angle(fer_pos, bet_pos) - angle(bet_pos, vul_pos)) <= epsilon()

def sunInTriangle(sun_pos, fer_pos, bet_pos, vul_pos):
	# The sun is inside the triangle formed by <fer_pos, bet_pos, vul_pos> if all 3 following turns:
	# - turn(sun_pos, fer_pos, bet_pos)
	# - turn(sun_pos, bet_pos, vul_pos)
	# - turn(sun_pos, vul_pos, fer_pos)
	# have the same sign (all positive or all negative)
	# If 1 or 2 of these turns is equal to 0, but the others is have the same sign, then the sun lies in the border
	#	of the triangle. In this case, we assume that it is inside
	turn1 = turn(sun_pos, fer_pos, bet_pos)
	turn2 = turn(sun_pos, bet_pos, vul_pos)
	turn3 = turn(sun_pos, vul_pos, fer_pos)
	return ((turn1 >= 0 and turn2 >= 0 and turn3 >= 0) or (turn1 <= 0 and turn2 <= 0 and turn3 <= 0))


def getFerengiPosition(day):
	return Point(cos(-day) * 500, sin(-day) * 500)

def getBetasoidPosition(day):
	return Point(cos(-3*day) * 2000, sin(-3*day) * 2000)

def getVulcanPosition(day):
	return Point(cos(5*day) * 1000, sin(5*day) * 1000)


def getPrecipitation(day):
	fer_pos = getFerengiPosition(day)
	bet_pos = getBetasoidPosition(day)
	vul_pos = getVulcanPosition(day)
	return areaTriangle(fer_pos, bet_pos, vul_pos)

def areaTriangle(A, B, C):
	distAB = dist(A, B)
	distBC = dist(B, C)
	distCA = dist(C, A)
	s = (distAB + distBC + distCA) / 2
	return sqrt(s * (s - distAB) * (s - distBC) * (s - distCA))

def dist(P, Q):
	return sqrt( (P.x - Q.x) * (P.x - Q.x) + (P.y - Q.y) * (P.y - Q.y) )