a = [1,2,3,4]
b = [10,20,30,40]

result = [0] * (len(a) + len(b))
result[::2] = a
result[1::2] = b

print(result)