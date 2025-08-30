# Abstraction
# Hiding the implementation details of a class ans only showing the essential features to the user
# abstraction is useful to reduce the complexity of the code and make the increase the usability
class Car:
    def __init__(self):
        self.__acc = False
        self.__brk = False
        self.__cluth = False
    
    def start(self):
        self.__cluth = True
        self.__acc=True
        return "you car is started"

car1 = Car()
print(car1.start())