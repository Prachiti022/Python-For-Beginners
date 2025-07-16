class Area:
    def calculate(self, a, b=None):
        if b is not None:
            print("Rectangle Area:", a * b)
        else:
            print("Square Area:", a * a)

# Creating an object
obj = Area()
obj.calculate(5)       # Square area
obj.calculate(5, 10)   # Rectangle area
