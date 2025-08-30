# age group categorization
def ageCategory(n):
    if(n<13):
        print("Child")
    elif(n>=13 and n<=19):
        print("Teenager")
    elif(n>=20 and n<=59):
        print("Adult")
    else:
        print("Senior")

n = int(input("Please enter your age: \n"))        
ageCategory(n)