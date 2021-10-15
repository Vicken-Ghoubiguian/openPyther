# Definition of the Weather class...
class Weather:

	# Definition of the Weather class constructor...
	def __init__(self, id, main, description, icon):

		self.__id = id
		self.__main = main
		self.__description = description
		self.__iconUrl = "https://openweathermap.org/img/wn/" + icon + ".png"

	#
	def getId(self):

		return self.__id

	#
	def getMain(self):

		return self.__main

	#
	def getDescription(self):

		return self.__description

	#
	def getIconUrl(self):

		return self.__iconUrl

	#
	def __str__(self):

		return "[id: " + self.__id + ", main: " + self.__main + ", description: " + self.__description + ", icon URL: " + self.__iconUrl + "]"