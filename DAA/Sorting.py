def counting_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Take user input for the array of integers
try:
    input_array = list(map(int, input("Enter the array of integers separated by space: ").split()))
    sorted_array = counting_sort(input_array)
    print("Sorted Array:", sorted_array)
except ValueError:
    print("Please enter valid integers.")
