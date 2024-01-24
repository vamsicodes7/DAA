
my_array = [1, 2, 3, 4, 5, 6, 7, 8]

max_sum = float("-inf")
max_sum_pair = None


for i in range(0, len(my_array), 2):

    if i + 1 < len(my_array):
        current_sum = my_array[i] + my_array[i + 1]
        
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_pair = (my_array[i], my_array[i + 1])

print("Maximum Sum:", max_sum)
print("Pair of Numbers:", max_sum_pair)
