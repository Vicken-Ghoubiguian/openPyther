# Definition of the Wind class...
class Wind:

	# Definition of the Wind class constructor...
	def __init__(self, speed, deg, gust):

		self.__speed = speed
		self.__deg = deg
		self.__gust = gust

	#
	def getSpeed(self):

		return self.__speed

	#
	def getDeg(self):

		return self.__deg

	#
	def getGust(self):

		return self.__gust

	#
	def __str__(self):

		return ""