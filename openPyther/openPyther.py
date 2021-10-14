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

				#
				print("YESSSSSSS....\n")

			#
			else:

				print("Nooooo....\n")

		#
		except:

			#
			self.__error = ""

			#
			print("Except...\n")

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
