# Sort the matrix without any inbuilt libararies 

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def sort_matrix(matrix):
    flattened_matrix = [item for sublist in matrix for item in sublist]
    flattened_matrix.sort()
    sorted_matrix = [flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(flattened_matrix), len(matrix[0]))]

    return sorted_matrix

def replace_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 0
        matrix[i][size - i - 1] = 0

    return matrix


matrix = get_matrix_from_user()


sorted_matrix = sort_matrix(matrix)


print("Sorted Matrix:")
print_matrix(sorted_matrix)


modified_matrix = replace_diagonals(sorted_matrix)


print("\nMatrix with Diagonals Replaced:")
print_matrix(modified_matrix)

