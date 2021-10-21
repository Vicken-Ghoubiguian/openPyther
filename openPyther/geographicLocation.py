# Definition of the GeographicLocation class...
class GeographicLocation:

	# Definition of the GeographicLocation class constructor...
	def __init__(self, countryCode, localisationName, utcOffsetAsTimestamp):

		self.__countryCode = countryCode
		self.__localisationName = localisationName
		self.__utcOffsetAsTimestamp = utcOffsetAsTimestamp

	# Definition of the country code's getter...
	def getCountryCode(self):

		return self.__countryCode

	# Definition of the localisation's getter...
	def getLocalisationName(self):

		return self.__localisationName

	# Definition of the UTC offset as timestamp's getter...
	def getUtcOffsetAsTimestamp(self):

		return self.__utcOffsetAsTimestamp

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):
		
		return "[{} ({})]".format(str(self.__localisationName), str(self.__countryCode))