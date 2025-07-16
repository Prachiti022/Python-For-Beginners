# Parent class created
class Parent:
    parentname = ""

    def show_parent(self):
        print(self.parentname)

# Child class created inherits Parent class
class Child(Parent):
    childname = ""

    def show_child(self):
        print(self.childname)

# Object of Child class
ch1 = Child()
ch1.parentname = "Vijay"  # Access Parent class attributes
ch1.childname = "Parth"
ch1.show_parent()  # Access Parent class method
ch1.show_child()  # Access Child class method
