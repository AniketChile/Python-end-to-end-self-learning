distance = int(input())
if(distance <3):
    transport = "walk"
elif(distance<=15):
    transport = "Bike"
else:
    transport = "Car"

print(transport)