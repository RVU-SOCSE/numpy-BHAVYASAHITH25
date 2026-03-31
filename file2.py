import numpy as np

# Create two matrices
A = np.array([[1, 2], 
              [3, 4]])

B = np.array([[5, 6], 
              [7, 8]])

print("Matrix A:\n", A)
print("\nMatrix B:\n", B)

# Addition
addition = A + B
print("\nMatrix Addition:\n", addition)

# Multiplication (matrix multiplication)
multiplication = np.dot(A, B)
print("\nMatrix Multiplication:\n", multiplication)

# Transpose
transpose_A = A.T
print("\nTranspose of Matrix A:\n", transpose_A)
