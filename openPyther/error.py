# Definition of the Error class...
class Error:

    # Definition of the Error class constructor...
    def __init__(self, code, message):

        self.__cod = code
        self.__message = message

    # Definition of the code's getter...
    def getCode(self):

        return self.__cod

    # Definition of the message's getter...
    def getMessage(self):

        return self.__message

    # Definition of the __str__ method to display the current object as a string...
    def __str__(self):
        
        return "{}: {}".format(str(self.__cod), str(self.__message))