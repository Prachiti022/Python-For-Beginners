import numpy as np

# Define two strings
str1 = np.array("Hello, ")
str2 = np.array("World!")

# Concatenate using NumPy
result = np.char.add(str1, str2)

print("Concatenated String:", result)
