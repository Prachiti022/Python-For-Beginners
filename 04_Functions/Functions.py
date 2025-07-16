
#FUNCTIONS
def func(name):                         #function with args
    print("Hi", name)
func("Prachiti")          

def add(a, b):                          #function with args
    print(a, " + ", b, " = ", a+b)
add(6, 2)

def add(a, b):                          #function with return value
    c = a+b
    return c
print("Enter two numbers: ")
x = int(input())
y = int(input())
z = add(x, y)
print(x, " + ", y, " = ", z)
#___________________________________________________________________________________________________________
