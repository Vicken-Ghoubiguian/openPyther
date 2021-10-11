# Importation of the Enum class to define the enum below...
from enum import Enum

# Definition of the UVRisk enum...
class UVRiskEnum(Enum):

	LOW = 1
	MODERATE = 2
	HIGH = 3
	VERY_HIGH = 4
	EXTREME = 5

# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, value):

		if value <= 2:

			determiedUVRisk = UVRiskEnum.LOW

		elif 3 <= value and value <= 5:

			determiedUVRisk = UVRiskEnum.MODERATE

		elif 6 <= value and value <= 7:
		
			determiedUVRisk = UVRiskEnum.HIGH

		elif 8 <= value and value <= 10:

			determiedUVRisk = UVRiskEnum.VERY_HIGH

		else:

			determiedUVRisk = UVRiskEnum.EXTREME

		self.__index = value
		self.__risk = determiedUVRisk

	#
	def getIndex(self):

		return self.__index

	#
	def getRisk(self):

		return self.__risk