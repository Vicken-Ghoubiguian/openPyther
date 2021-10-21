#
from . import UVRiskEnum

# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, lon, lat):

		self.__index = 0

		#
		if self.__index <= 2:

			determiedUVRisk = UVRiskEnum.LOW

		#
		elif 3 <= self.__index and self.__index <= 5:

			determiedUVRisk = UVRiskEnum.MODERATE

		#
		elif 6 <= self.__index and self.__index <= 7:
		
			determiedUVRisk = UVRiskEnum.HIGH

		#
		elif 8 <= self.__index and self.__index <= 10:

			determiedUVRisk = UVRiskEnum.VERY_HIGH

		#
		else:

			determiedUVRisk = UVRiskEnum.EXTREME

		#
		self.__risk = determiedUVRisk

	# Definition of the index's getter...
	def getIndex(self):

		return self.__index

	# Definition of the risk's getter...
	def getRisk(self):

		return self.__getRiskAsString()

	#
	def __getRiskAsString(self):

		#
		if self.__risk == UVRiskEnum.LOW:

			return "Low"

		#
		elif self.__risk == UVRiskEnum.MODERATE:

			return "Moderate"

		#
		elif self.__risk == UVRiskEnum.HIGH:

			return "High"

		#
		elif self.__risk == UVRiskEnum.VERY_HIGH:

			return "Very high"

		#
		else:

			return "Extreme"

	# Definition of the __str__ method to display the current object as a string...
	def __str__(self):

		return "{} ({})".format(str(self.__index), str(self.__getRiskAsString()))
