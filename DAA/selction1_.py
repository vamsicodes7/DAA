def selectSort(l):
    n = len(l)
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            if l[j] < l[min_ind]:
                min_ind = j
                l[min_ind], l[i] = l[i], l[min_ind]
l = [10, 5, 8, 20, 2, 18]
selectSort(l)
print(*l)