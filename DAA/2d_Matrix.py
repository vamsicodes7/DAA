import numpy as np

x = np.arange(1, 17).reshape(4, 4)
print(x)
output = []


for i in range(4):
    output.append(x[0, i])
for i in range(1, 4):
    output.append(x[i, -1])
for i in range(2, -1, -1):
    output.append(x[-1, i])
for i in range(2, 0, -1):
    output.append(x[i, 0])

print(output)

