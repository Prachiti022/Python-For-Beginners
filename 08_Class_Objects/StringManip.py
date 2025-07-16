class StringManipulator:
    def get_String(self):
        self.text = input("Enter a string: ")

    def print_String(self):
        print(self.text.upper())

# Example usage
obj = StringManipulator()
obj.get_String()
obj.print_String()
