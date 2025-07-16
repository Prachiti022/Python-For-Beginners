class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width

# Example usage
rect = Rectangle(5, 10)
print("Area of Rectangle:", rect.compute_area())  # Output: 50
