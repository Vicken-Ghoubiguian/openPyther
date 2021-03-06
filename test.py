# Import the main module to use the OpenPyther class (main class)...
import openPyther.openPyther as openPyther

# Import the 'sys' module to use arguments...
import sys

# Initialization of the 'openPyther' object with the wished localisation, the wished country code and the OpenWeather API key as parameters...
openPytherObject = openPyther.OpenPyther(sys.argv[1], sys.argv[2], sys.argv[3])

# Display the 'openPyther' object as a string...
print(openPytherObject)
