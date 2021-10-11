# Importation of the Enum class to define the enum below...
from enum import Enum

# Definition of the Pressure enum...
class PressureEnum(Enum):

	HECTOPASCAL = 1
	PASCAL = 2
	BAR = 3
	ATMOSPHERE = 4
	TORR = 5
	POUNDSPERSQUAREINCH = 6

# Definition of the Pressure class...
class Pressure:

	#
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = PressureEnum.HECTOPASCAL
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