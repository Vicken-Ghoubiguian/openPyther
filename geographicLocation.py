# Definition of the GeographicLocation class...
class GeographicLocation:

	# Definition of the GeographicLocation class constructor...
	def __init__(self, countryCode, cityName):

		self.__countryCode = countryCode
		self.__cityName = cityName

	#
	def getCountryCode(self):

		return self.__countryCode

	#
	def getCityName(self):

		return self.__cityName		