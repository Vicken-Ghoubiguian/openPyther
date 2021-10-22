#
from . import UVRiskEnum

# Import the installed-from-PyPi module named "requests" to elaborate and execute HTTP/HTTPS requests...
import requests

# Import the module named "json" to jsonify, dejsonify and treat JSON datas and strings...
import json

# Definition of the UV class...
class UV:

	# Definition of the UV class constructor...
	def __init__(self, APIKey, lat, lon):

		self.__index = 0

		#
		uvResponse = requests.get("https://api.openweathermap.org/data/2.5/uvi?appid=" + APIKey + "&lat=-49.35&lon=70.2167", None)

		print(uvResponse.text)

		#
		#uvResponse_datas = json.loads(uvResponse.text)

		#
		#self.__index = uvResponse_datas["value"]
		self.__index = 0

		#
		#self.__dateAsTimestamp = uvResponse_datas["date"]

		#
		#self.__dateISO = uvResponse_datas["date_iso"]

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
