#
from . import temperatureEnum

# Definition of the Temperature class...
class Temperature:

	# Definition of the Temperature class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

	#
	def getValue(self):

		return self.__value

	#
	def getMeasureUnit(self):

		return self.__measureUnit

	#
	def __getSymbolUnit(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "K"

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "°C"

		#
		else:

			return "°F"

	#
	def __getMeasureUnitAsString(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "Kelvin"

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "Celsius"

		#
		else:

			return "Fahrenheit"

	#
	def setTemperatureAsKelvin(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			#
			self.__value = self.__value + 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

			#
			print("\nTemperature converted from Celsius (°C) to Kelvin (K)\n")

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.FAHRENHEIT:

			#
			self.__value = (self.__value - 32) * (5.0/9.0) + 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

			#
			print("\nTemperature converted from Fahrenheit (°F) to Kelvin (K)\n")

		#
		else:

			#
			print("\nTemperature already in Kelvin (K)\n")

	#
	def setTemperatureAsCelsius(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			#
			self.__value = self.__value - 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.CELSIUS

			#
			print("\nTemperature converted from Kelvin (K) to Celsius (°C)\n")

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.FAHRENHEIT:

			#
			self.__value = (self.__measureUnit - 32) * (5.0/9.0)
			self.__measureUnit = temperatureEnum.TemperatureEnum.CELSIUS

			#
			print("\nTemperature converted from Fahrenheit (°F) to Celsius (°C)\n")

		#
		else:

			#
			print("\nTemperature already in Celsius (°C)\n")

	#
	def setTemperatureAsFahrenheit(self):

		#
		if self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			#
			self.__value = (self.__value * (9.0/5.0)) + 32
			self.__measureUnit = temperatureEnum.TemperatureEnum.FAHRENHEIT

			#
			print("\nTemperature converted from Celsius (°C) to Fahrenheit (°F)\n")

		#
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			#
			self.__value = (self.__value - 273.15) * (9.0/5.0) + 32
			self.__measureUnit = temperatureEnum.TemperatureEnum.FAHRENHEIT

			#
			print("\nTemperature converted from Kelvin (K) to Fahrenheit (°F)\n")

		#
		else:

			#
			print("\nTemperature already in Fahrenheit (°F)\n")
	
	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "{} {} ({})".format(str(self.__value), str(self.__getSymbolUnit()), str(self.__getMeasureUnitAsString()))