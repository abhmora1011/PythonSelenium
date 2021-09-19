# This is a comment in python

print("Hello World")

a, b = 2, 4.2

# print("The sum of a and b is: " + (a + b)) //ERROR

print("{} {}".format("The sum of a and b is : ", a + b))

print(type(a))

print(type(b))

#list can hold multiple values with differect data types

listType = [12, 234, "However", 2.35]

print(listType[0]) # Print first element

print(listType[-1]) # Print last element

print(listType[1:3]) # Print substring index 1 up to but included 3

listType.insert(3, 'Hello') # inserting an item

listType.insert(2, 'Abe')

del listType[2] # deleting an item

print(listType) #

print(listType[1:3])

#tuple can hold multiple values with differect data types but immutable means we cannot change what is declared

thisType = (12, 234, "However", 2.35)

#thisType[1] = 2 error

print(thisType)

#dictionary is a key value pair

thisDictionary = {"Hello": 2, "Hi": 4, 1: "Sea"}

print(thisDictionary["Hello"])



