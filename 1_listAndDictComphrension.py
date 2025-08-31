# list and dictornay comprehnsion are easy and more concise way of creating the list and dictonary in the python. using the iterable object .
# in list comphrension we can create the new list by applying the expression on each item of the iterable also hecking the condition if required

# in the dict comphresionas the key 0value pair is required in dictornay we use the  key value pair from an iterable

# list comprehension example
# list1 = [x**2 for x in range(1,11)]
# print(list1)

# dictonary comprehension example
dict1 = {x:x**2 for x in range(1,11)}
print(dict1)

# traditionalWay in list
# list2 = []
# for item in range(1,11):
#     list2.append(item*item)

# print(list2)

# traditional way in dictonary
# dict2 ={}
# for key in range(1,11):
#     dict2[key]=key*key

# print(dict2)

# list2 = [x for x in range(1,11) if x%2 == 0]
# print(list2)