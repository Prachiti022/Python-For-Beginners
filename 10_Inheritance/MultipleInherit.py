# Class for addition
class Add:
    def Addition(self, a, b):
        return a + b

# Class for multiplication
class Mul:
    def Multiplication(self, a, b):
        return a * b

# Derived class inheriting Add and Mul
class Derived(Add, Mul):
    def Divide(self, a, b):
        return a / b

# Object of Derived class
d = Derived()
print(d.Addition(10, 20))
print(d.Multiplication(10, 20))
print(d.Divide(10, 20))
