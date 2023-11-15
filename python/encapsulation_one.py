class Student:
    def __init__(self, name, rollNumber):
        
        self.__name = name
        self.__rollNumber = rollNumber

    
    def getName(self):
        return self.__name

    def getRollNumber(self):
        return self.__rollNumber

    
    def setName(self, name):
        self.__name = name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber