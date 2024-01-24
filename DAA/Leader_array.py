def leader(array, size):
    i = 0
    while i < size:
        j = i + 1
        while j < size:
            if array[i] <= array[j]:
                break
            j += 1
        if j == size:
            print(array[i], end=" ")
        i += 1

array = [16, 17, 4, 3, 5, 2]
result = leader(array, len(array))

