class Rectangle:
    def __init__(self, length=1, breadth=1):
        self.length = length
        self.breadth = breadth

# Creating objects with different numbers of arguments
rect1 = Rectangle()
print(rect1.length, rect1.breadth)

rect2 = Rectangle(5)
print(rect2.length, rect2.breadth)

rect3 = Rectangle(5, 10)
print(rect3.length, rect3.breadth)
