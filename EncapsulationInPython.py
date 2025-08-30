# Encapsulation
# Wrapping data and Functions into a single unit(object)
# the encapsulation is one of the pillar of the oops the encapsulation protect the internal state of an object from getting modified by directly accessing the data it prevents from dirrect access so that the data is safe and ensure unintenionally modification
# it also provide the controlled way to access or change the data with the object attributes

class EmployeeSalary:
    def __init__(self,name,salary):
        self.__name = name
        self.__salary = salary
    
    def getFullInfo(self):
        return f"the emp name is {self.__name} & his salary is {self.__salary}"    
    
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def changeName(self,name):
        if isinstance(name, str):
            self.__name = name
        else:
            print("invalid input")
    
    def changeSalary(self,salary):
        if(salary < 1000):
             print("Invalid Salary")
        else:
            self.__salary = salary
            print(f"salary changed succesffully to {self.__salary}")

emp1 = EmployeeSalary("Aniket",10000)     
# emp1.__name = "Rahil"
print(emp1.__name)
# emp1._EmployeeSalary__salary = 500000

print(emp1.getName())
print(emp1.getFullInfo())