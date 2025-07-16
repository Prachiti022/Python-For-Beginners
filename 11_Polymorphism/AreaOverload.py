class Shape:
    def area(self, length, breadth=None):
        if breadth is not None:
            print("Rectangle Area:", length * breadth)
        else:
            print("Square Area:", length * length)

# Creating an object
s = Shape()
s.area(4)        # Square
s.area(4, 6)     # Rectangle
