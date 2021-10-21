# Definition of the Weather class...
class Weather:

	# Definition of the Weather class constructor...
	def __init__(self, id, main, description, icon):

		self.__id = id
		self.__main = main
		self.__description = description
		self.__iconUrl = "https://openweathermap.org/img/wn/" + icon + "@2x.png"

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

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "[id: {}, main: {}, description: {}, icon URL: {}]".format(str(self.__id), str(self.__main), str(self.__description), str(self.__iconUrl))