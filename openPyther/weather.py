# Definition of the Weather class...
class Weather:

	# Definition of the Weather class constructor...
	def __init__(self, id, main, description, icon):

		self.__id = id
		self.__main = main
		self.__description = description
		self.__iconUrl = "https://openweathermap.org/img/wn/" + icon + "@2x.png"

	# Definition of the id's getter...
	def getId(self):

		return self.__id

	# Definition of the main's getter...
	def getMain(self):

		return self.__main

	# Definition of the description's getter...
	def getDescription(self):

		return self.__description

	# Definition of the url of icon's getter...
	def getIconUrl(self):

		return self.__iconUrl

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "[id: {}, main: {}, description: {}, icon URL: {}]".format(str(self.__id), str(self.__main), str(self.__description), str(self.__iconUrl))