# Import the module which contains the pressure units enum...
from . import pressureEnum

# Definition of the Pressure class...
class Pressure:

	# Definition of the Pressure class constructor...
	def __init__(self, value):

		self.__value = value
		self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

	# Definition of the hectoPascal's converter...
	def setPressureAsHectoPascal(self):

		# In the case where the current unit is Pascal...
		if self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

			self.__value = self.__value / 100
			self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

			print("\nPressure converted from Pascal (Pa) to hectoPascal (hPa)\n")

		# In the case where the current unit is Bar...
		elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

			self.__value = self.__value * 1000
			self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

			print("\nPressure converted from Bar (bar) to hectoPascal (hPa)\n")

		# In the case where the current unit is Atmosphere...
		elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

			self.__value = self.__value * 1013.2501
			self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

			print("\nPressure converted from Atmosphere (atm) to hectoPascal (hPa)\n")

		# In the case where the current unit is Torr...
		elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

			self.__value = self.__value * 1.333223684211
			self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

			print("\nPressure converted from Torr (torr) to hectoPascal (hPa)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		elif self.__measureUnit == pressureEnum.PressureEnum.POUNDSPERSQUAREINCH:

			self.__value = self.__value * 68.9475729318
			self.__measureUnit = pressureEnum.PressureEnum.HECTOPASCAL

			print("\nPressure converted from Pounds Per Square Inch (psi) to hectoPascal (hPa)\n")

		# In the case where the current unit is hectoPascal...
		else:

			print("\nPressure already in hectoPascal (hPa)\n")

	# Definition of the Pascal's converter...
	def setPressureAsPascal(self):

		# In the case where the current unit is hectoPascal...
		if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

			self.__value = self.__value * 100
			self.__measureUnit = pressureEnum.PressureEnum.PASCAL

			print("\nPressure converted from hectoPascal (hPa) to Pascal (Pa)\n")

		# In the case where the current unit is Bar...
		elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

			self.__value = self.__value * 100000
			self.__measureUnit = pressureEnum.PressureEnum.PASCAL

			print("\nPressure converted from Bar (bar) to Pascal (Pa)\n")

		# In the case where the current unit is Atmosphere...
		elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

			self.__value = self.__value * 101325
			self.__measureUnit = pressureEnum.PressureEnum.PASCAL

			print("\nPressure converted from Atmosphere (atm) to Pascal (Pa)\n")

		# In the case where the current unit is Torr...
		elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

			self.__value = self.__value * 133.3223684211
			self.__measureUnit = pressureEnum.PressureEnum.PASCAL

			print("\nPressure converted from Torr (torr) to Pascal (Pa)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		elif self.__measureUnit == pressureEnum.PressureEnum.POUNDSPERSQUAREINCH:

			self.__value = self.__value * 6894.7572931783
			self.__measureUnit = pressureEnum.PressureEnum.PASCAL

			print("\nPressure converted from Pounds Per Square Inch (psi) to Pascal (Pa)\n")

		# In the case where the current unit is Pascal...
		else:

			print("\nPressure already in Pascal (Pa)\n")

	# Definition of the Bar's converter...
	def setPressureAsBar(self):

		# In the case where the current unit is hectoPascal...
		if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

			print("\nPressure converted from hectoPascal (hPa) to Bar (bar)\n")

		# In the case where the current unit is Pascal...
		elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

			print("\nPressure converted from Pascal (pa) to Bar (bar)\n")

		# In the case where the current unit is Atmosphere...
		elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

			print("\nPressure converted from Atmosphere (atm) to Bar (bar)\n")

		# In the case where the current unit is Torr...
		elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

			print("\nPressure converted from Torr (torr) to Bar (bar)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		elif self.__measureUnit == pressureEnum.PressureEnum.POUNDSPERSQUAREINCH:

			print("\nPressure converted from Pounds Per Square Inch (psi) to Bar (bar)\n")

		# In the case where the current unit is Bar...
		else:

			print("\nPressure already in Bar (bar)\n")

	# Definition of the Atmosphere's converter...
	def setPressureAsAtmosphere(self):

		# In the case where the current unit is hectoPascal...
		if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

			self.__value = self.__value / 1013.25
			self.__measureUnit = pressureEnum.PressureEnum.ATMOSPHERE

			print("\nPressure converted from hectoPascal (hPa) to Atmosphere (atm)\n")

		# In the case where the current unit is Pascal...
		elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

			self.__value = self.__value / 101325
			self.__measureUnit = pressureEnum.PressureEnum.ATMOSPHERE

			print("\nPressure converted from Pascal (pa) to Atmosphere (atm)\n")

		# In the case where the current unit is Bar...
		elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

			self.__value = self.__value / 1.01325
			self.__measureUnit = pressureEnum.PressureEnum.ATMOSPHERE

			print("\nPressure converted from Bar (bar) to Atmosphere (atm)\n")

		# In the case where the current unit is Torr...
		elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

			self.__value = self.__value / 760
			self.__measureUnit = pressureEnum.PressureEnum.ATMOSPHERE

			print("\nPressure converted from Torr (torr) to Atmosphere (atm)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		elif self.__measureUnit == pressureEnum.PressureEnum.POUNDSPERSQUAREINCH:

			self.__value = self.__value / 14.696
			self.__measureUnit = pressureEnum.PressureEnum.ATMOSPHERE

			print("\nPressure converted from Pounds Per Square Inch (psi) to Atmosphere (atm)\n")

		# In the case where the current unit is Atmosphere...
		else:

			print("\nPressure already in Atmosphere (atm)\n")


	# Definition of the Torr's converter...
	def setPressureAsTorr(self):

		# In the case where the current unit is Pascal...
		if self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

			self.__value = self.__value / 133.32236842
			self.__measureUnit = pressureEnum.PressureEnum.TORR

			print("\nPressure converted from Pascal (Pa) to to Torr (torr)\n")

		# In the case where the current unit is Bar...
		elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

			self.__value = self.__value * 750.061682704
			self.__measureUnit = pressureEnum.PressureEnum.TORR

			print("\nPressure converted from Bar (bar) to to Torr (torr)\n")

		# In the case where the current unit is Atmosphere...
		elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

			self.__value = self.__value * 760
			self.__measureUnit = pressureEnum.PressureEnum.TORR

			print("\nPressure converted from Atmosphere (atm) to Torr (torr)\n")

		# In the case where the current unit is hectoPascal...
		elif self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

			self.__value = self.__value / 1.3332236842
			self.__measureUnit = pressureEnum.PressureEnum.TORR

			print("\nPressure converted from hectoPascal (hPa) to Torr (torr)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		elif self.__measureUnit == pressureEnum.PressureEnum.POUNDSPERSQUAREINCH:

			self.__value = self.__value * 51.715
			self.__measureUnit = pressureEnum.PressureEnum.TORR

			print("\nPressure converted from Pounds Per Square Inch (psi) to Torr (torr)\n")

		# In the case where the current unit is Torr...
		else:

			print("\nPressure already in Torr (torr)\n")

	# Definition of the Pounds per square inch's converter...
	def setPressureAsPoundsPerSquareInch(self):

		# In the case where the current unit is hectoPascal...
		if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

			self.__value = self.__value / 68.94757293168
			self.__measureUnit = pressureEnum.PressureEnum.POUNDSPERSQUAREINCH

			print("\nPressure converted from hectoPascal (hPa) to Pounds Per Square Inch (psi)\n")

		# In the case where the current unit is Pascal...
		elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

			self.__value = self.__value / 6894.757293168
			self.__measureUnit = pressureEnum.PressureEnum.POUNDSPERSQUAREINCH

			print("\nPressure converted from Pascal (Pa) to Pounds Per Square Inch (psi)\n")

		# In the case where the current unit is Bar...
		elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

			self.__value = self.__value * 14.503773773022
			self.__measureUnit = pressureEnum.PressureEnum.POUNDSPERSQUAREINCH

			print("\nPressure converted from Bar (bar) to Pounds Per Square Inch (psi)\n")

		# In the case where the current unit is Atmosphere...
		elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

			self.__value = self.__value * 14.695964
			self.__measureUnit = pressureEnum.PressureEnum.POUNDSPERSQUAREINCH

			print("\nPressure converted from Atmosphere (atm) to Pounds Per Square Inch (psi)\n")

		# In the case where the current unit is Torr...
		elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

			self.__value = self.__value / 51.715
			self.__measureUnit = pressureEnum.PressureEnum.POUNDSPERSQUAREINCH

			print("\nPressure converted from Torr (torr) to Pounds Per Square Inch (psi)\n")

		# In the case where the current unit is Pounds Per Square Inch...
		else:

			print("\nPressure already in Pounds Per Square Inch (psi)\n")

	# Definition of the value's getter...
	def getValue(self):

		return self.__value

	# Definition of the measure unit's getter...
	def getMeasureUnit(self):

		return self.__measureUnit

	# Definition of a class method which returns the unit of measure's symbol as a string...
	def __getSymbolUnit(self):

			#
			if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

				return "hPa"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

				return "Pa"

			# In the case where the current unit is Bar...
			elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

				return "bar"

			# In the case where the current unit is Atmosphere...
			elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

				return "atm"

			#
			elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

				return "torr"

			#
			else:

				return "psi"

	# Definition of a class method which returns the unit of measure as a string...
	def __getMeasureUnitAsString(self):

			# In the case where the current unit is hectoPascal...
			if self.__measureUnit == pressureEnum.PressureEnum.HECTOPASCAL:

				return "hectoPascal"

			# In the case where the current unit is Pascal...
			elif self.__measureUnit == pressureEnum.PressureEnum.PASCAL:

				return "Pascal"

			# In the case where the current unit is Bar...
			elif self.__measureUnit == pressureEnum.PressureEnum.BAR:

				return "Bar"

			# In the case where the current unit is Atmosphere...
			elif self.__measureUnit == pressureEnum.PressureEnum.ATMOSPHERE:

				return "Atmosphere"

			# In the case where the current unit is Torr...
			elif self.__measureUnit == pressureEnum.PressureEnum.TORR:

				return "Torr"

			# In the case where the current unit is Pound per square inch...
			else:

				return "Pound per square inch"

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "{} {} ({})".format(str(self.__value), str(self.__getSymbolUnit()), str(self.__getMeasureUnitAsString()))