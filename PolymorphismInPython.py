class Ax:
    def __hello(self):
        print("Hello user")
        
    def welcome(self):
        return self.__hello()
    
person = Ax()
print(person.welcome())