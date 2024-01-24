import numpy as np

binary_matrix = np.array([
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
])

# Sum of the middle row
middle_row_sum = np.sum(binary_matrix[len(binary_matrix)//2, :])

# Sum of the middle column
middle_col_sum = np.sum(binary_matrix[:, len(binary_matrix[0])//2])

print(f"Sum of the middle row: {middle_row_sum}")
print(f"Sum of the middle column: {middle_col_sum}")
