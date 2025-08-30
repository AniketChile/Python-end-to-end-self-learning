petSpecies = str(input()).capitalize()
age = int(input())
if(petSpecies == "Dog"):
    if(age<2):
        print("Puppy Food")
    else:
        print("Adult food food")
elif (petSpecies == "Cat"):
    if(age<=5):
        print("young cat food")
    elif(age>5):
        print("senior cat food")    
else:
    print("This pet is not yet recognized")    