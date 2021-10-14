#
from . import UVRiskEnum

# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, value):

		self.__index = value

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

		self.__risk = determiedUVRisk

	#
	def getIndex(self):

		return self.__index

	#
	def getRisk(self):

		return self.__risk

	#
	def __str__(self):

		return ""