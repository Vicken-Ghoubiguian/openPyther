# Definition of the Time class...
class Time:

    # Definition of the Time class constructor...
    def __init__(self, sunriseAsTimestampAccordingToUtc, sunsetAsTimestampAccordingToUtc, utcOffsetAsTimestamp):
        
        #
        self.__utcOffsetAsTimestamp = utcOffsetAsTimestamp

        #
        self.__sunriseAsTimestampAccordingToUtc = sunriseAsTimestampAccordingToUtc
        self.__sunsetAsTimestampAccordingToUtc = sunsetAsTimestampAccordingToUtc
        
        #
        self.__sunriseAsTimestampAccordingTheirTimezone = self.__sunriseAsTimestampAccordingToUtc + self.__utcOffsetAsTimestamp
        self.__sunsetAsTimestampAccordingTheirTimezone = self.__sunsetAsTimestampAccordingToUtc + self.__utcOffsetAsTimestamp

    #
    def getSunriseAsTimestampAccordingToUtc(self):

        return self.__sunriseAsTimestampAccordingToUtc

    #
    def getSunsetAsTimestampAccordingToUtc(self):

        return self.__sunsetAsTimestampAccordingToUtc

    #
    def getSunriseAsTimestampAccordingTheirTimezone(self):

        return self.__sunriseAsTimestampAccordingTheirTimezone

    #
    def getSunsetAsTimestampAccordingTheirTimezone(self):

        return self.__sunsetAsTimestampAccordingTheirTimezone

    # Definition of the __str__ method to display the current object as a string...
    def __str__(self):
        
        return ""