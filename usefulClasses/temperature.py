#
from usefulEnums import TemperatureEnum

# Definition of the Temperature class...
class Temperature:

	# Definition of the Temperature class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = TemperatureEnum.Temperature.KELVIN
		self.__measureUnitSymbol = "K"

	#
	def getValue(self):

		return self.__value

	#
	def getMeasureUnit(self):

		return self.__measureUnit

	#
	def getSymbolUnit(self):

		return self.__measureUnitSymbol

	#
	def setTemperatureAsKelvin(self):

		print("Conversion in Kelvin...")

	#
	def setTemperatureAsCelsius(self):

		print("Conversion in Celsius...")

	#
	def setTemperatureAsFahrenheit(self):

		print("Conversion in Fahrenheit...")