# Import the module which contains the pressure units enum...
from . import pressureEnum

# Definition of the Pressure class...
class Pressure:

	# Definition of the Pressure class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

	#
	def setPressureAsHectoPascal(self):

		print("Conversion in HectoPascal...")

	#
	def setPressureAsPascal(self):

		print("Conversion in Pascal...")
	#
	def setPressureAsBar(self):

		print("Conversion in Bar...")

	#
	def setPressureAsAtmosphere(self):

		print("Conversion in Atmosphere...")

	#
	def setPressureAsTorr(self):

		print("Conversion in Torr...")

	#
	def setPressureAsPoundsPerSquareInch(self):

		print("Conversion in Pounds Per Square Inch...")

	#
	def getValue(self):

		return self.__value

	#
	def getMeasureUnit(self):

		return self.__measureUnit

	#
	def __getSymbolUnit(self):

			#
			if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

				return "hPa"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

				return "Pa"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

				return "bar"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

				return "atm"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

				return "torr"

			#
			else:

				return "psi"

	#
	def __getMeasureUnitAsString(self):

			#
			if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

				return "hectoPascal"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

				return "Pascal"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

				return "Bar"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

				return "Atmosphere"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

				return "Torr"

			#
			else:

				return "Pound per square inch"

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "{} {} ({})".format(str(self.__value), str(self.__getSymbolUnit()), str(self.__getMeasureUnitAsString()))