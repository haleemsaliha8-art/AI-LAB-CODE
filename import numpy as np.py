import numpy as np
print(np.__version__)
array = np.array([[0, 1], [2, 3]])

print("Original array:")
print(array)
flattened_array = array.flatten()
print("\nFlattened array:")
print(flattened_array)
max_value = np.max(flattened_array)
min_value = np.min(flattened_array)
print("\nMaximum value of the above flattened array:", max_value)
print("Minimum value of the above flattened array:", min_value)