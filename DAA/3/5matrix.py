def sum_middle_row_and_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    middle_row = rows // 2
    middle_col = cols // 2

    middle_value = matrix[middle_row][middle_col]

    row_sum = sum(matrix[middle_row])
    col_sum = sum(row[middle_col] for row in matrix) 
    total_sum = row_sum + col_sum - middle_value
    return total_sum

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

result = sum_middle_row_and_column(matrix)
print("Sum of middle row and middle column values (excluding middle value):",result)