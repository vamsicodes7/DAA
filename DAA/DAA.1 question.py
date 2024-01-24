N, D = map(int, input().split())
l = []

for i in range(N):
    l1 = list(map(int, input().split()))
    l.append(l1)

curse = 0
x = True
day = 1
d = 1

while x:
    l1 = []
    if day == D + 1:
        break

    for i in l:
        if i[1] == 0:
            l.remove(i)

    for i in range(len(l)):
        if l[i][0] == day:
            l1.append(l[i])

    min_val = -999

    for i in l1:
        if i[2] > min_val:
            min_val = i[2]
            temp = i

    for i in range(len(l)):
        if l[i] == temp:
            l[i][0] += 1
            l[i][1] -= 1
        elif l[i] in l1:
            l[i][0] += 1

    day += 1

for i in l:
    if i[1] != 0:
        curse += i[1] * i[2]

print(curse)


