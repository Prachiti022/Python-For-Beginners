import numpy as np

# Creating a 2D matrix
matrix = np.array([[10, 20, 30], [40, 50, 60]])
print("Original Matrix:\n", matrix)

# Transpose of the matrix
transpose_matrix = matrix.T
print("Transpose of Matrix:\n", transpose_matrix)

# Reshaping the matrix
reshaped_matrix = matrix.reshape(3, 2)
print("Reshaped Matrix (3x2):\n", reshaped_matrix)
