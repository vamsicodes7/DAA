def count_ones(row):
    return row.count(1)

def find_max_ones(matrix):
    max_ones = 0
    max_row = -1

    for i, row in enumerate(matrix):
        ones_count = count_ones(row)
        if ones_count > max_ones:
            max_ones = ones_count
            max_row = i

    return max_row

matrix = []
print("Please enter a 4x4 matrix with only 1s and 0s (with spaces between each no.s):")
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

max_row = find_max_ones(matrix)

if max_row != -1:
    print(f"The row with the highest number of 1s is Row = {max_row+1}")
    print(f"Number of 1s: {matrix[max_row].count(1)}")
else:
    print("No row contains any 1s.")