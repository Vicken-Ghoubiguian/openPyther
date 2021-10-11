#
from usefulEnums import UVRiskEnum

# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, value):

		if value <= 2:

			determiedUVRisk = UVRiskEnum.UVRiskEnum.LOW

		elif 3 <= value and value <= 5:

			determiedUVRisk = UVRiskEnum.UVRiskEnum.MODERATE

		elif 6 <= value and value <= 7:
		
			determiedUVRisk = UVRiskEnum.UVRiskEnum.HIGH

		elif 8 <= value && value <= 10:

			determiedUVRisk = UVRiskEnum.UVRiskEnum.VERY_HIGH

		else:

			determiedUVRisk = UVRiskEnum.UVRiskEnum.EXTREME

		self.__index = value
		self.__risk = determiedUVRisk

	#
	def getIndex(self):

		return self.__index

	#
	def getRisk(self):

		return self.__risk