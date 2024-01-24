def remove(arr):
    x = []
    for i in arr:
        if i not in x:
            x.append(i)

    return x

array = [0,0,0,0,0,]
y = remove(array)
print(y)

# def remove(arr):
#     x = []
#     return [x for i, x in enumerate(arr) if x not in arr[:i]]

# my_array = [1, 2, 2, 3, 4, 4, 5]
# y = remove(my_array)
# print(y)
