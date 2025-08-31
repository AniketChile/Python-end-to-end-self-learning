# iterator
# list1 = [1,2,3,4,5,6]
# It = iter(list1)
# print(It.__next__())

# Generator
def countNum(n):
    count = 1
    while (count <= n):
        yield count
        count+=1

for number in countNum(10):
    print(number,end=" ")