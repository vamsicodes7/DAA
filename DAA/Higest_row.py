import numpy as np
matrix = [
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 0, 0, 1]
]
matrix = np.array(matrix)
row_sum = np.sum(matrix, axis=1)
max_row = np.argmax(row_sum)
print(f"Row {max_row + 1} has the maximum sum of {row_sum[max_row]}")
