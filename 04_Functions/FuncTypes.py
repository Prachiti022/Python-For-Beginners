# Function with positional arguments
def pos_args(a, b):
    print(f"Positional Args: a = {a}, b = {b}")

# Function with keyword arguments
def kw_args(real, imag):
    print(f"Complex Number: {complex(real, imag)}")

# Function with default arguments
def default_args(x, y=50):
    print(f"x: {x}, y: {y}")

# Function with variable-length arguments (*args)
def var_length_args(*args):
    print("Variable Length Args:", args)

# Function with variable-length keyword arguments (**kwargs)
def var_length_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")

# Pass by reference demonstration
def pass_by_ref(x):
    print(f"Value received: {x}, id: {id(x)}")

# Driver code
pos_args(3, 5)  
kw_args(real=3, imag=5)  
kw_args(imag=5, real=3)  

default_args(10)  

var_length_args('Hello', 'Python', 'World')  
var_length_kwargs(first='Python', second='is', third='Awesome')

# Pass by reference example
x = 12
print(f"Value passed: {x}, id: {id(x)}")
pass_by_ref(x)

