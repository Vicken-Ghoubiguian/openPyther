# Import the temperature units enum...
from . import temperatureEnum

# Definition of the Temperature class...
class Temperature:

	# Definition of the Temperature class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

	# Definition of the value's getter...
	def getValue(self):

		return self.__value

	# Definition of the unit of measure's getter...
	def getMeasureUnit(self):

		return self.__measureUnit

	# Definition of a class method which returns the unit of measure's symbol as a string...
	def __getSymbolUnit(self):

		# In the case where the current unit is Kelvin...
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "K"

		# In the case where the current unit is Celsius...
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "°C"

		# In the case where the current unit is Fahrenheit...
		else:

			return "°F"

	# Definition of a class method which returns the unit of measure as a string...
	def __getMeasureUnitAsString(self):

		# In the case where the current unit is Kelvin...
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			return "Kelvin"

		# In the case where the current unit is Celsius...
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			return "Celsius"

		# In the case where the current unit is Fahrenheit... 
		else:

			return "Fahrenheit"

	# Definition of the Kelvin's converter...
	def setTemperatureAsKelvin(self):

		# In the case where the current unit is Celsius...
		if self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			# Calculus of conversion from Celsius to Kelvin...
			self.__value = self.__value + 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

			print("\nTemperature converted from Celsius (°C) to Kelvin (K)\n")

		# In the case where the current unit is Fahrenheit...
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.FAHRENHEIT:

			# Calculus of conversion from Fahrenheit to Kelvin...
			self.__value = (self.__value - 32) * (5.0/9.0) + 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.KELVIN

			print("\nTemperature converted from Fahrenheit (°F) to Kelvin (K)\n")

		# Or in the case where the current unit is Kelvin...
		else:

			print("\nTemperature already in Kelvin (K)\n")

	# Definition of the Celsius's converter...
	def setTemperatureAsCelsius(self):

		# In the case where the current unit is Kelvin...
		if self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			# Calculus of conversion from Kelvin to Celsius...
			self.__value = self.__value - 273.15
			self.__measureUnit = temperatureEnum.TemperatureEnum.CELSIUS

			print("\nTemperature converted from Kelvin (K) to Celsius (°C)\n")

		# In the case where the current unit is Fahrenheit...
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.FAHRENHEIT:

			# Calculus of conversion from Fahrenheit to Celsius...
			self.__value = (self.__measureUnit - 32) * (5.0/9.0)
			self.__measureUnit = temperatureEnum.TemperatureEnum.CELSIUS

			print("\nTemperature converted from Fahrenheit (°F) to Celsius (°C)\n")

		# Or in the case where the current unit is Celsius...
		else:

			print("\nTemperature already in Celsius (°C)\n")

	# Definition of the Fahrenheit's converter...
	def setTemperatureAsFahrenheit(self):

		# In the case where the current unit is Celsius...
		if self.__measureUnit == temperatureEnum.TemperatureEnum.CELSIUS:

			# Calculus of conversion from Celsius to Fahrenheit...
			self.__value = (self.__value * (9.0/5.0)) + 32
			self.__measureUnit = temperatureEnum.TemperatureEnum.FAHRENHEIT

			print("\nTemperature converted from Celsius (°C) to Fahrenheit (°F)\n")

		# In the case where the current unit is Kelvin...
		elif self.__measureUnit == temperatureEnum.TemperatureEnum.KELVIN:

			# Calculus of conversion from Kelvin to Fahrenheit...
			self.__value = (self.__value - 273.15) * (9.0/5.0) + 32
			self.__measureUnit = temperatureEnum.TemperatureEnum.FAHRENHEIT

			print("\nTemperature converted from Kelvin (K) to Fahrenheit (°F)\n")

		# Or in the case where the current unit is Fahrenheit...
		else:

			print("\nTemperature already in Fahrenheit (°F)\n")
	
	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "{} {} ({})".format(str(self.__value), str(self.__getSymbolUnit()), str(self.__getMeasureUnitAsString()))