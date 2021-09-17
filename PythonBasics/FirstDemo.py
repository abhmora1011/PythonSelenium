# This is a comment in python

print("Hello World")

a, b = 2, 4.2

# print("The sum of a and b is: " + (a + b)) //ERROR

print("{} {}".format("The sum of a and b is : ", a + b))

print(type(a))

print(type(b))

#list can hold multiple values with differect data types

listType = [12, 234, "However", 2.35]

print(listType[0])

print(listType[-1])

print(listType[1:3])

listType.insert(3, 'Hello')

listType.insert(2, 'Abe')

print(listType)

print(listType[1:3])

#tuple

thisType = (12, 234, "However", 2.35)

#thisType[1] = 2 error

print(thisType)

#dictionary

thisDictionary = {"Hello": 2, "Hi": 4, 1: "Sea"}

print(thisDictionary["Hello"])



