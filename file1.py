import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original Array:")
print(arr)

# Reshape the array (2 rows, 3 columns)
reshaped_arr = arr.reshape(2, 3)
print("\nReshaped Array (2x3):")
print(reshaped_arr)

# Indexing (access element)
print("\nElement at index [1][2]:", reshaped_arr[1][2])

# Sum of elements
total_sum = arr.sum()
print("\nSum of all elements:", total_sum)
