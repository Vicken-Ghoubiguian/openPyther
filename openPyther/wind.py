# Definition of the Wind class...
class Wind:

	# Definition of the Wind class constructor...
	def __init__(self, speed, deg):

		self.__speed = speed
		self.__deg = deg

	#
	def getSpeed(self):

		return self.__speed

	#
	def getDeg(self):

		return self.__deg

	#
	def __str__(self):

		return ""