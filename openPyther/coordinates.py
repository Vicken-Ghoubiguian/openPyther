# Definition of the Coordinates class...
class Coordinates:

	# Definition of the Coordinates class constructor...
	def __init__(self, longitude, latitude):

		self.__longitude = longitude
		self.__latitude = latitude

	# Definition of the longitude's getter...
	def getLongitude(self):

		return self.__longitude

	# Definition of the latitude's getter...
	def getLatitude(self):

		return self.__latitude

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "(longitude: {}, latitude: {})".format(str(self.__longitude), str(self.__latitude))