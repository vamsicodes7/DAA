def row_with_most_ones(matrix):
    max_ones_row = -1
    max_ones_count = -1

    for i, row in enumerate(matrix):
        ones_count = row.count(1)
        if ones_count > max_ones_count:
            max_ones_count = ones_count
            max_ones_row = i

    return max_ones_row

binary_matrix = [
    [0, 1, 1, 1],
    [0, 0, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1]
]

result = row_with_most_ones(binary_matrix)

if result != -1:
    print(f"Row with the most ones is Row {result + 1}")
else:
    print("No ones found in the matrix.")
