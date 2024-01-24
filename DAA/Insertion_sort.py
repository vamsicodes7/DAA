def insertion_sort(list):
    for i in range(1, len(list)):
        current_element = list[i]
        j = i - 1
        while j >= 0 and list[j] > current_element:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = current_element
    return list

print(insertion_sort([0,0,1,2,0,1,2,2,1]))