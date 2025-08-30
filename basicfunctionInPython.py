# sqare a number in the function
# n = 5

# def squareWhat(n):
#     return n**2

# print(squareWhat(n))

# Create a function that takes two numbers as parameter and returns their sum
# def sumOfTwoNumber(a,b):
#     return a+b

# ans = sumOfTwoNumber(5,2)
# print(ans)

# Polymorphism Function 
# Write a function multiply that multiplies two numbers, but can also accept and multiply strings

# def multiply(para1,para2):
#     return para1 * para2

# inp1 = 10
# string2 = "chile"
# string3 = multiply(inp1,string2)
# print(string3)

# write a function that returns the both area and the circumfernce of a circle given its radius
# import math
# def area_and_circumfernce_of_circle(radiusParamter):
#     areaOfCircle = round(math.pi * radiusParamter ** 2,2)
#     circumferenceOfACircle = round(2 * math.pi * radiusParamter,2)
#     return [areaOfCircle,circumferenceOfACircle]

# li = area_and_circumfernce_of_circle(2)
# print("area ",li[0]," "," circumfernce of the circle: ",li[1])

# import math
# def area_and_circumfernce_of_circle(radiusParamter):
#     areaOfCircle = round(math.pi * radiusParamter ** 2,2)
#     circumferenceOfACircle = round(2 * math.pi * radiusParamter,2)
#     return areaOfCircle,circumferenceOfACircle

# area , circumference = area_and_circumfernce_of_circle(2)
# print("area ",area," "," circumfernce of the circle: ",circumference)

# Write a function that greets a user. If no name is provided, it should greet with a default name
# def geetUser(name = "User"):
#     return "Hello, "+ name + " !"

# print(geetUser("chai"))

# Create a lambda function to compute the cube of a number
# cube = lambda x : x ** 3
# anotheCurbe = cube
# anotheCurbe = lambda y : y ** 4
# print(cube(5)) 
# print(anotheCurbe(6))

# write a function that takes variable number of arguments and returns their sum
# function with *args
# takes as such arguments are getting pass in args name can be changes iterable args are basically tuple
# def sum_all(*args):#/*superman(*-is important)): 
#     ans = 0
#     print(type(args))
#     for i in args:
#         ans += i
#     return ans

# print(sum_all(1,2,3))
# print(sum_all(1,2,6,3,6,5,8,9,6,54,1,2))
# print(sum_all(1,2))

# write a function that accepts any number of keyword arguments and prins them in teh format key:value
# function with **kwargs

# def comic(**kwargs):
    
#     print(type(kwargs),kwargs)

# comic(name="Shaktiman",power="laser")
# comic(name="Hatim")
# comic(name = "Hero",power="Bhakti hi shakti hai")

# Generator function with yield 
# yield keyword is using which basically store the value + their state in the memory so suppose any two method are call python handle the situtation easily
# def even_num_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i
        
# for num in even_num_generator(10):
#     print(num)

# print("*************_________________**************")

# for num in even_num_generator(20):
#     print(num)        

# recursive function
# create a recursive function to calculate the factorial of a number

# ******************Understanding Scope***********************

# def factorial_using_recursive(num):
#     if(num == 1):
#         return num
#     return num * factorial_using_recursive(num-1)

# a = factorial_using_recursive(5)
# print(a)

# def recursive_func(num):
#     if(num == 1):
#         return num
#     return num * recursive_func(num-1)
#     # return ans
# result = recursive_func(5)
# print(result)

# x = 99
# def func3():
#     x = 56
#     return x 

# func3()
# print(x)

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()

# closures
# x = 99
# def f1():
#     x = 88
#     def f2():
#         global x
#         x = 5
#     return f2

# result = f1()
# print(result())
# print(x)
# *******************Closure*******************
# def chaicoder(nums):
#     def actual(x):
#         return x ** nums
#     return actual

# f = chaicoder(2)
# g = chaicoder(3)

# print(f(3))
# print(g(3))
# ****************Closure*************************
