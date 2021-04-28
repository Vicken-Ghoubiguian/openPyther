# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, value):

		determiedUVRisk = ""

		if value <= 2:

			determiedUVRisk = "Low"

		elif 3 <= value and value <= 5:

			determiedUVRisk = "Moderate"

		elif 6 <= value and value <= 7:
		
			determiedUVRisk = "High"

		elif 8 <= value && value <= 10:

			determiedUVRisk = "Very High"

		else:

			determiedUVRisk = "Extreme"

		self.__index = value
		self.__risk = determiedUVRisk

	#
	def getIndex(self):

		return self.__index

	#
	def getRisk(self):

		return self.__risk		