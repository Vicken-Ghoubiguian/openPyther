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
    def __str__(self):
        
        return ""