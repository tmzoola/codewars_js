class Person:

    __passport_number="AA7286123"

    def __init__(self,name,job):
        self.__name = name
        self.job = job

    def getName(self):
        return self.__name
    

    def setName(self,newName):
        self.__name=newName

    def getPassport(self):
        return self.__passport_number

    
        

person = Person("Murodjon","Developer")

print(person.getPassport())