def greet(name):
    print("Good morning " + name)


greet("Abe")


def getType(sample):
    return type(sample)


def addition(first, second):
    valid = type(1)

    if getType(first) != valid:
        print("Invalid Type for input 1")
    elif getType(second) != valid:
        print("Invalid Type for input 2")
    else:
        print(first + second)


addition(2, "one")
