# Import all modules useful for the main class (OpenPyther class)...
from . import Coordinates
from . import GeographicLocation
from . import Humidity
from . import Pressure
from . import Temperature
from . import UV
from . import Weather
from . import Wind
from . import Error

# Import the installed-from-PyPi module named "requests" to elaborate and execute HTTP/HTTPS requests...
import requests

# Import the module named "json" to jsonify, dejsonify and treat JSON datas and strings...
import json

# Definition of the OpenPyther class...
class OpenPyther:

	# Definition of the first OpenPyther class constructor...
	def __init__(self, city, countryCode, APIKey):

		#
		try:

			#
			weatherResponse = requests.post("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&appid=" + APIKey + "", None)

			#
			weatherResponse_datas = json.loads(weatherResponse.text)

			# Definition of the 'Cod' attribute (which correspond to the previous HTTP/HTTPS response's cod)...
			self.__cod = weatherResponse_datas["cod"]

			#
			if self.__cod == 200:

				"""
				Initialisation of coordinates...
				"""
				self.__coordinates = Coordinates(longitude = weatherResponse_datas["coord"]["lon"], latitude = weatherResponse_datas["coord"]["lat"])

				"""
				"""
				self.__temperature = Temperature(value = weatherResponse_datas["main"]["temp"])
				self.__feeling_like_temperature = Temperature(value = weatherResponse_datas["main"]["feels_like"])
				self.__minimum_temperature = Temperature(value = weatherResponse_datas["main"]["temp_min"])
				self.__maximum_temperature = Temperature(value = weatherResponse_datas["main"]["temp_max"])

				""" 
				Treatments for UTC offset, localisation and country code...
				"""
				self.__utcOffsetAsTimestamp = weatherResponse_datas["timezone"]
				self.__localisationName = weatherResponse_datas["name"]
				self.__countryCode = weatherResponse_datas["sys"]["country"]

				#
				print(str(self.__coordinates))
				print(str(self.__temperature))

			#
			else:

				#
				self.__error = Error(self.__cod, weatherResponse_datas["message"])

		#
		except:

			#
			self.__error = ""

	#
	def getCod(self):

		return self.__cod

	#
	def getCoords(self):

		print("getCoords function...")

	#
	def getWeather(self):

		print("getWeather function...")

	#
	def getTemperature(self):

		print("getTemperature function...")

	#
	def getFeelingLikeTemperature(self):

		print("getFeelingLikeTemperature function...")

	#
	def getMinTemperature(self):

		print("getMinTemperature function...")

	#
	def getMaxTemperature(self):

		print("getMaxTemperature function...")

	#
	def getPressure(self):

		print("getPressure function...")

	#
	def getHumidity(self):

		print("getHumidity function...")

	#
	def getWind(self):

		print("getWind function...")

	#
	def getSunrise(self):

		print("getSunrise function...")

	#
	def getSunset(self):

		print("getSunset function...")

	#
	def getGeographicLocation(self):

		print("getGeographicLocation function...")

	#
	def getUltraViolet(self):

		print("getUltraViolet function...")

	#
	def getError(self):

		return self.__error

	#
	def __str__(self):

		return ""
