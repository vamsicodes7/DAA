def multiply_recursive(a, b):

    if a == 0 or b == 0:
        return 0

 
    return a + multiply_recursive(a, b - 1)

num1 = 5
num2 = 3

result = multiply_recursive(num1, num2)
print(f"{num1} * {num2} = {result}")
