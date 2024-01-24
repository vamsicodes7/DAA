import numpy as np
def swap_diagonal_corners(matrix):
    n = len(matrix)
    for i in range(n):
        if i == 0 or i == n - 1:
            matrix[i][i], matrix[i][n - i - 1] = matrix[i][n - i - 1], matrix[i][i]
    return matrix

original_matrix = np.arange(0,9).reshape(3,3)
print("Original matrix : ")
for row in original_matrix:
    print(" ".join(map(str, row)))

print("Swapped Matrix :")
output_matrix = swap_diagonal_corners(original_matrix)
for row in output_matrix:
    print(" ".join(map(str, row)))
