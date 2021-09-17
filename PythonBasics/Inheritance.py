from ObjectOrientedProgramming import Calculator


class Child(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 10, 5) # Call the constructor of the Parent Class

    def getSomething(self):
        return self.num + self.num2 + self.subtract()


obj = Child()

print(obj.getSomething())
