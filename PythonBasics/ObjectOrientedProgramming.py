class Calculator:

    # self is only for local scope  self.num
    # Class name is for global scope Calculator.num or self.num

    num = 100

    def __init__(self, a, b):  # To create a constructor
        self.firstNumber = a
        self.secondNumber = b
        print("Constructor Triggered")

    def add(self):
        print("I'm not executing a method inside a class")

    def subtract(self):
        var = (self.firstNumber - self.secondNumber) * self.num
        # var = (self.firstNumber - self.secondNumber) * Calculator.num
        return var

obj = Calculator(5, 3)  # instantiate an object
obj.add()
print(obj.subtract())
print(obj.num)
