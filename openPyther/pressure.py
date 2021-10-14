#
from . import pressureEnum

# Definition of the Pressure class...
class Pressure:

	#
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL
		self.__measureUnitSymbol = "hPa"

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
	def getSymbolUnit(self):

		return self.__measureUnitSymbol

	#
	def __str__(self):

		return ""		