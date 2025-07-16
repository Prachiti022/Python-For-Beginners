import numpy as np

# Creating two matrices
A = np.array([[2, 4], [6, 8]])
B = np.array([[1, 3], [5, 7]])

# Addition
add_result = A + B
print("Addition:\n", add_result)

# Subtraction
sub_result = A - B
print("Subtraction:\n", sub_result)

# Multiplication (Element-wise)
mul_result = A * B
print("Multiplication:\n", mul_result)

# Division (Element-wise)
div_result = A / B
print("Division:\n", div_result)
