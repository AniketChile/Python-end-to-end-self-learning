passwordString = len(str(input()))
if(passwordString < 6):
    print("weak password")
elif(passwordString>=6 and passwordString<=10):
    print("medium password")
else:
    print("strong password")