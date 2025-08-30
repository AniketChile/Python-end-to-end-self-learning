# the init is the constructor of the class which is invoked when the instance of that class i.e the object is been created.
# self is the paramater which is used in the init function which is the refernce of the current object and usign self we can assign the attributes to the instance
class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
car1 = Vehicle("Tata","Nexon")
car2 = Vehicle("Tesla","Model S")
car3 = Vehicle("Martui","800")
print(car1.brand)