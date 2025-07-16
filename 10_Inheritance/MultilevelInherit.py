# GrandParent class created
class GrandParent:
    grandparentname = ""

    def show_grandparent(self):
        print(self.grandparentname)

# Parent class created
class Parent(GrandParent):
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
ch1.grandparentname = "Vaibhav"  # Access GrandParent class attributes
ch1.parentname = "Vijay"  # Access Parent class attributes
ch1.childname = "Parth"
ch1.show_grandparent()  # Access GrandParent class method
ch1.show_parent()  # Access Parent class method
ch1.show_child()  # Access Child class method
