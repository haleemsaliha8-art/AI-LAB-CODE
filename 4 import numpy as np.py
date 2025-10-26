import numpy as np

# Define two 2x2 matrices
A = np.array([[5, 5],
              [1, 1]])

B = np.array([[2, 0],
              [1, 2]])

# Multiply the matrices
result = np.dot(A, B)

# Take the transpose of the resultant matrix
transpose_result = result.T

# Display results
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
print("\nResult of A x B:")
print(result)
print("\nTranspose of the resultant matrix:")
print(transpose_result)
