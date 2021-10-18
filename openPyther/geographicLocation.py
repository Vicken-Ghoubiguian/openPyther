# Definition of the GeographicLocation class...
class GeographicLocation:

	# Definition of the GeographicLocation class constructor...
	def __init__(self, countryCode, localisationName, utcOffsetAsTimestamp):

		self.__countryCode = countryCode
		self.__localisationName = localisationName
		self.__utcOffsetAsTimestamp = utcOffsetAsTimestamp

	#
	def getCountryCode(self):

		return self.__countryCode

	#
	def getLocalisationName(self):

		return self.__localisationName

	#
	def getUtcOffsetAsTimestamp(self):

		return self.__utcOffsetAsTimestamp

	#
	def __str__(self):
		
		return "{} ({})".format(str(self.__localisationName), str(self.__countryCode))