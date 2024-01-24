num = int(input("Enter the Length of the array: "))
a = []
for i in range(num):
    nums = int(input("Enter the Numbers: "))
    a.append(nums)

max_value = max(a)  

result = [0] * (max_value + 1)

for num in a:
    result[num] = num

_result = [0] + [i for i in range(1, max_value + 1)] 

print(_result)
