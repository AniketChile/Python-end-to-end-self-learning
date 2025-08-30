# the class attibutes are the data which is acess by the object which is created from that class
# where is the object attribut is only accesible to the object of the class so that no other class can access that

class Vechile:
    Vehicle = "Tony Garage"
    def __init__(self,name,model):
        self.name = name
        self.model = model
s1 = Vechile("Tata","Nexon")
s2 = Vechile("Bmw","S3")
print(s1.model,s1.name,s1.Vehicle)
print(s2.model,s2.name,s2.Vehicle)
# s3 = Vechile()
print(Vechile.Vehicle)