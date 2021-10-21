# Definition of the Wind class...
class Wind:

	# Definition of the Wind class constructor...
	def __init__(self, speed, deg):

		self.__speed = speed
		self.__deg = deg

	# D
	def getSpeed(self):

		return self.__speed

	#
	def getDeg(self):

		return self.__deg

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return ""
