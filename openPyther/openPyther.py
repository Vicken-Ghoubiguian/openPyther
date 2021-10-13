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

#
import requests

#
import json

# Definition of the OpenPyther class...
class OpenPyther:

	# Definition of the first OpenPyther class constructor...
	def __init__(self, city, countryCode, APIKey):

		#
		weatherResponse = requests.post("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&appid=" + APIKey + "", None)
		
		#
		print(type(weatherResponse))

		#
		print(type(weatherResponse.text))

		print(weatherResponse.text)

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
