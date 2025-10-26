import numpy as np

A = np.array([
    [6, 1, 1, 3],
    [4, -2, 5, 1],
    [2, 8, 7, 6],
    [3, 1, 9, 7]
], dtype=float)

invA = np.linalg.inv(A)
print("Inverse of A:")
print(np.round(invA, 6))

# Verify: A @ invA should be identity
print("\nA @ invA (rounded):")
print(np.round(A.dot(invA), 6))
