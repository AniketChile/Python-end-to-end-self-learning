class Car:
    totalCar = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Car.totalCar += 1
    
    # example of abstraction
    def fullName(self):
        return f"{self.__brand} {self.__model}"
    
    # polymorphism example
    def fuelType(self):
        return "Petrol or Diesel"
    
    
    @staticmethod
    def fullInfo():
        return 'the car milage is less'

    @property
    def model(self):
        return self.__model
    

# inheritance example 
class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size
     
     # polymorphism example   
    def fuelType(self):
        return "Electric charge"

myTesla = ElectricCar("tesla","model s","85kwh")
# print(myTesla.fuelType())

safari = Car("Tata","Safari")
# print(safari.fuelType())
# safari.__model = "Apple"
print(safari.model)

# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())

# myNewCar= Car("Tata","Safari")
# print(myNewCar.brand)
# print(myNewCar.model)

