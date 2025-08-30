string_s = "Hello World"
# charString = list(string_s)

# left = 0
# right = len(charString)-1
# while(left < right):
#     charString[left],charString[right] = charString[right],charString[left]
#     left+=1
#     right-=1

# string_s = "".join(charString)
# print(string_s)

# print(string_s[::-1])
reversedS = ""
for char in string_s:
    reversedS = char + reversedS
print(reversedS)