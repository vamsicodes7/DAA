def time_com(n, c, f, g):
    for num in n:
        if f(num) < c * g(num):
            return False
    return True

def f(n):
    return n

def g(n):
    return 3*n+2


n = [1,2,3,4,5,6]
c = 0.1

result = time_com(n, c, f,g)
print(result)