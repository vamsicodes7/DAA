def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        
    
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
                
 
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [0,0,1,2,0,1,2,2,1]
selection_sort(arr)
print("Sorted array:", arr)
