import numpy as np

def rotate_matrix(matrix):
    n = len(matrix)
    rotated_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_matrix[n - j - 1][i] = matrix[i][j]

    return rotated_matrix

original_matrix = np.arange(1, 10).reshape(3, 3)
print("Original Matrix:")
print(original_matrix)

rotated_matrix = rotate_matrix(original_matrix)
print("\nRotated Matrix:")
for row in rotated_matrix:
    print(" ".join(map(str, row)))
