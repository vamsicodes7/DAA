def sort_matrix_and_replace_diagonals(matrix):
   
    def sort_matrix(mat):
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            for j in range(cols - 1):
                for k in range(0, cols - j - 1):
                    if mat[i][k] > mat[i][k + 1]:
                        mat[i][k], mat[i][k + 1] = mat[i][k + 1], mat[i][k]

    
    def replace_diagonals_with_zeros(mat):
        rows, cols = len(mat), len(mat[0])
        for i in range(rows):
            mat[i][i] = 0 
            mat[i][cols - 1 - i] = 0 

    
    sort_matrix(matrix)

 
    replace_diagonals_with_zeros(matrix)


matrix = [
    [4, 2, 7],
    [1, 5, 9],
    [8, 3, 6]
]


print("Original Matrix:")
for row in matrix:
    print(row)

sort_matrix_and_replace_diagonals(matrix)

print("\nModified Matrix:")
for row in matrix:
    print(row)
