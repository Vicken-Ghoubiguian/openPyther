# Import all modules useful for the main class (OpenPyther class)...
from . import Coordinates
from . import GeographicLocation
from . import Humidity
from . import Pressure
from . import Temperature
from . import UV
from . import Time
from . import Weather
from . import Wind
from . import OpenWeatherError

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
			weatherResponse = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "," + countryCode + "&appid=" + APIKey + "", None)

			#
			weatherResponse_datas = json.loads(weatherResponse.text)

			# Definition of the 'Cod' attribute (which correspond to the previous HTTP/HTTPS response's cod)...
			self.__cod = weatherResponse_datas["cod"]

			# In the case where the HTTPS request is successed (when the response's code is equal to 200)...
			if self.__cod == 200:

				"""
				Initialisation of coordinates...
				"""
				self.__coordinates = Coordinates(longitude = weatherResponse_datas["coord"]["lon"], latitude = weatherResponse_datas["coord"]["lat"])

				"""
				Initialisations of weather...
				"""
				self.__weather = Weather(id = weatherResponse_datas["weather"][0]["id"], main = weatherResponse_datas["weather"][0]["main"], description = weatherResponse_datas["weather"][0]["description"], icon = weatherResponse_datas["weather"][0]["icon"])

				"""
				Initialisations of all temperatures and treatments for them...
				"""
				self.__temperature = Temperature(value = weatherResponse_datas["main"]["temp"])
				self.__feeling_like_temperature = Temperature(value = weatherResponse_datas["main"]["feels_like"])
				self.__minimum_temperature = Temperature(value = weatherResponse_datas["main"]["temp_min"])
				self.__maximum_temperature = Temperature(value = weatherResponse_datas["main"]["temp_max"])

				"""
				Initialisation of pressure and treatments for it...
				"""
				self.__pressure = Pressure(value = weatherResponse_datas["main"]["pressure"])

				"""
				Initialisation of all wind datas...
				"""
				self.__wind = Wind(speed = weatherResponse_datas["wind"]["speed"], deg = weatherResponse_datas["wind"]["deg"])

				"""
				Initialisation for humidity...
				"""
				self.__humidity = Humidity(value = weatherResponse_datas["main"]["humidity"])

				"""
				Initialisation for geographic locations...
				"""
				self.__geographicLocation = GeographicLocation(countryCode = weatherResponse_datas["sys"]["country"], localisationName = weatherResponse_datas["name"], utcOffsetAsTimestamp = weatherResponse_datas["timezone"])

				"""
				Initialisation for UV...
				"""
				self.__uv = UV(APIKey = APIKey, lat = weatherResponse_datas["coord"]["lat"], lon = weatherResponse_datas["coord"]["lon"])

				"""
				Treatments for sunrise and sunset times...
				"""
				self.__time = Time(sunriseAsTimestampAccordingToUtc = weatherResponse_datas["sys"]["sunrise"], sunsetAsTimestampAccordingToUtc = weatherResponse_datas["sys"]["sunset"], utcOffsetAsTimestamp = weatherResponse_datas["timezone"])

			# In the other case (when the response's code is not equal to 200 - when an OpenWeather error occured)...
			else:

				"""
				Initialisation of the OpenWeatherError error and raise it...
				"""
				raise OpenWeatherError(self.__cod, weatherResponse_datas["message"])

		#
		except ConnectionError as occuredError:

			"""
			Raise the occured error named "occuredError"...
			"""
			raise occuredError

	# Definition of the code's getter...
	def getCod(self):

		return self.__cod

	# Definition of the coordinates' getter...
	def getCoords(self):

		return self.__coordinates

	# Definition of the weather's getter...
	def getWeather(self):

		return self.__weather

	# Definition of the current temperature's getter...
	def getTemperature(self):

		return self.__temperature

	# Definition of the feeling like temperature's getter...
	def getFeelingLikeTemperature(self):

		return self.__feeling_like_temperature

	# Definition of the expected minimum temperature's getter...
	def getMinTemperature(self):

		return self.__minimum_temperature

	# Definition of the expected maximum temperature's getter...
	def getMaxTemperature(self):

		return self.__maximum_temperature

	# Definition of the pressure's getter...
	def getPressure(self):

		return self.__pressure

	# Definition of the humidity's getter...
	def getHumidity(self):

		return self.__humidity

	# Definition of the wind's getter...
	def getWind(self):

		return self.__wind

	# Definition of the geographic location's getter...
	def getGeographicLocation(self):

		return self.__geographicLocation

	# Definition of the time's getter...
	def getTime(self):

		return self.__time

	# Definition of the UV (UltraViolet)'s getter...
	def getUV(self):

		return self.__uv

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		#
		return "\n" + 	"\033[4m" + "Coordinates" + ":\033[0m " + str(self.__coordinates) + "\n" + \
							"\033[4m" + "Weather" + ":\033[0m " + str(self.__weather) + "\n" + \
							"\033[4m" + "Geographic location" + ":\033[0m " + str(self.__geographicLocation) + "\n" + \
							"\033[4m" + "Temperature" + ":\033[0m " + str(self.__temperature) + "\n" + \
							"\033[4m" + "Feeling like temperature" + ":\033[0m " + str(self.__feeling_like_temperature) + "\n" + \
							"\033[4m" + "Minimum expected temperature" + ":\033[0m " + str(self.__minimum_temperature) + "\n" + \
							"\033[4m" + "Maximum expected temperature" + ":\033[0m " + str(self.__maximum_temperature) + "\n" + \
							"\033[4m" + "Pressure" + ":\033[0m " + str(self.__pressure) + "\n" + \
							"\033[4m" + "Humidity" + ":\033[0m " + str(self.__humidity) + "\n" + \
							"\033[4m" + "Wind" + ":\033[0m " + str(self.__wind) + "\n" + \
							"\033[4m" + "UV" + ":\033[0m " + str(self.__uv) + "\n" + \
							"\033[4m" + "Time" + ":\033[0m " + str(self.__time) + "\n"