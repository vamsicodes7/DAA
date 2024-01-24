## Leader Numbers : In the array, considering the right numbers, we need to check if left number is 
# biggest than the right side numbers

## In a given array, we need to extract the greatest elements if the niumbers after them are smaller thamn that number

def leader_numbers(arr):
    n = len(arr)                     # len(arr) givens the no. of elements of the array
    leaders = [ ]
    max_right = arr[n - 1]           # Displays (n-1)th index of the array since index starts from 0 to n
    
    leaders.append(max_right)        # Rightmost or last element of the array is the leader number always 
                                     # because there are no numbers after it to compare
    for i in range(n - 2, -1, -1) :
        if arr[i] > max_right: 
            max_right = arr[i]
            leaders.append(max_right)
        
    return leaders[::-1]
    
sample = [16, 17, 4, 3, 5, 2]
result = leader_numbers(sample)
print("Leader Numbers:",result)


###################################################################

# Input - Array
# Output - Small No. , Big No. , ....

def SmallNoBigNo(arr, n):                                 # Zig Zag Numbers
    arr.sort()                                            # using sort function to sort the array
    for i in range(1, n-1, 2):                            # traverse the array from 1 to n-1
        arr[i], arr[i+1] = arr[i+1], arr[i]               # swap value of current element with next element
    print(arr)


if __name__ == "_main_":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    SmallNoBigNo(arr,n)

 ####################################################################################################

 # Triplet Numbers and thei Sum

# Ex : 

## A = [1, 2, 3, 4, 5]

# Sum needs to be 9 ; add any three no.s from the above array, their sum needs to 9

# 2 + 3 + 5 = 9
# 1 + 3 + 5 = 9


def find_triplets_with_sum(arr, target_sum):
    n = len(arr)
    found_triplets = []

    # Sort the array for better efficiency
    arr.sort()

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:                                       
            # whule loop is only for condition checking.... it doesnt stay till the end
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                found_triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return found_triplets

# Example usage:
user_sum = int(input("Enter the target sum: "))
user_array = list(map(int, input("Enter space-separated numbers in the array: ").split()))

triplets = find_triplets_with_sum(user_array, user_sum)

if triplets:
    print("Triplets with the sum", user_sum, "are:")
    for triplet in triplets:
        print(triplet)
else:
    print("No triplets found with the given sum.")



#################################################################################################

# Given array : [0, 0, 1, 2, 0, 1, 2, 2, 1]

# Output : [0, 0, 0, 1, 1, 1, 2, 2, 2]



# Sorting using 

def default_sort(a):
    n = len(a)       # Length of the Array

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them again
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]      # Here no.s are swapped

# Input array
a = [0, 0, 1, 2, 0, 1, 2, 2, 1]

# Call the custom_sort function to sort the array
custom_sort(a)

# Display the sorted array
print("Sorted Array : ", a)

# Time Complexity : n^2


######################################################################################################


# Removing Duplicate Values
def remove_dup_values(input_list):
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

user_input = input("Enter a list of numbers separated by commas: ")
user_list = [int(x) for x in user_input.split(',')]

result_list = remove_dup_values(user_list)

print("Original List:", user_list)
print("List with Duplicates Removed:",result_list)

# Write a code to know whether your code has a loop or not

class Node:
    def _init_(self, k):
        self.key = k
        self.next = None
        
def InsertBegin(head, key):                   
    temp = Node(key)
    temp.next = head 
    return temp

head = None
head = InsertBegin(head, 10)
head = InsertBegin(head, 20)
head = InsertBegin(head, 50)
head = InsertBegin(head, 40)

def printList(head):                           
    curr = head
    while curr != None:
        print(curr.key, end = " ")
        curr = curr.next
        
printList(head)


####################################################################################################

# Merge Sort

# Time Complexity : N log N

# Normal while loop where i, i, i = N
# if there is patterns like i/2 = log N
# if there is a loop i and then another loop in it i.e., iteration or is there is while loop = N log N


def merge_sort(arr, start, end):
    
    if start < end:                
# start < end, thsi is due to if there is a single element in the array, 
# starting index = ending index and then if there is a single element, there is nothing to sort in the array.
# So, to avoid that condition we make sure starting index is less than ending index
        mid = (start + end) // 2

        # Sort the first/left half
        merge_sort(arr, start, mid)

        # Sort the second half
        merge_sort(arr, mid + 1, end)

        # Merge the two sorted halves
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    left_half = arr[start:mid + 1]
    right_half = arr[mid + 1:end + 1]

    i = j = 0
    k = start

    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1

    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

# Example Usage
arr = list(map(int, input("Enter space-separated numbers in the array: ").split()))
merge_sort(arr, 0, len(arr)-1)
print(arr)



###################################################################################################

def find_max_sum_subsets(arr):
    n = len(arr)
    max_sum = float("-inf")
    max_subsets = []

    # Generate all possible subsets of the array
    for i in range(1 << n):
        subset = [arr[j] for j in range(n) if (i & (1 << j)) > 0]

        # Calculate the sum of the current subset
        current_sum = sum(subset)

        # Check if the current sum is greater than the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
            max_subsets = [subset]
        elif current_sum == max_sum:
            max_subsets.append(subset)

    return max_sum, max_subsets

# Example usage
user_input = input("Enter the array elements separated by spaces: ")
arr = list(map(int, user_input.split()))
max_sum, max_subsets = find_max_sum_subsets(arr)

print("Maximum Sum:", max_sum)
print("Different Possible Element Sets:")
for subset in max_subsets:
 print(subset)

 ######################################################

 # Interchange the Diagonal

#  0 1 2                        2 1 0
#  3 4 5    ---------------->   3 4 5
#  6 7 8                        8 7 6

# Input : [0, 4, 8] is the LEFT diagonal & [2, 4, 6] is the RIGHT diagonal
# Output : [0, 4, 8] is the RIGHT diagonal & [2, 4, 6] is the LEFT diagonal

# Trick : Swap the corners

def interchange_diagonals(matrix):
    n = len(matrix)          # len(matrix) gives the number of rows in the matrix i.e., n = 3
    for i in range(n):
        matrix[i][i], matrix[i][n-i-1] = matrix[i][n-i-1], matrix[i][i]   # Swapping the corners
        # since we are representing the no.s & matrix in the form of array, the indexing starts from 0, 1, 2...
    return matrix

original_matrix = [[0, 1, 2], 
                   [3, 4, 5], 
                   [6, 7, 8]]
result_matrix = interchange_diagonals(original_matrix)

for row in result_matrix:
    print(row)
    
## For i = 0:
# matrix[0][0], matrix[0][2] = matrix[0][2], matrix[0][0]
# This swaps the elements in the first row: matrix[0][0] = (0) & matrix[0][2] = (2).

## For i = 1:
# matrix[1][1], matrix[1][1] = matrix[1][1], matrix[1][1]
# This is effectively a no-op. It doesn't change the matrix.

##For i = 2:
# matrix[2][2], matrix[2][0] = matrix[2][0], matrix[2][2]
# This swaps the elements in the third row: matrix[2][2] (8) and matrix[2][0] (6).

################################################################################################

# Display the index no. in the array by finding that number in the array

# A[i] = i

def index_array(A):
    n = len(A)
    
    for i in range(n): 
        while A[i] != i:               # != - not equal to
            temp = A[i]
            A[i], A[temp] = A[temp], A[i]
    return A

A = [2, 3, 1, 0, 4, 5, 7, 6, 9, 8]
result = index_array(A)
print(result)


def index_array(A):
    n = len(A)
    
    for i in range(n): 
# This line starts a loop that iterates over the indices from 0 to n-1. 
# In each iteration, i will take on one of these values.
        while A[i] != i:               # != - not equal to
# This line starts a while loop. It continues as long as the element at index i in the list A is not equal to i. 
# This condition checks if the element at index i is in its correct position.
            temp = A[i]
# Inside the while loop, this line assigns the value of A[i] to the variable temp. 
# This temporarily stores the value of the element at index i.
            A[i], A[temp] = A[temp], A[i]
# This line swaps the values at indices i and temp in the list A. 
# This effectively moves the element to its correct position.
    return A

A = [2, 3, 1, 0, 4, 5, 7, 6, 9, 8]
result = index_array(A)
print(result)

# In summary, this code takes a list as input, and for each element in the list, 
# it swaps the element with the element at its correct index until all elements are in their correct positions. 
# The modified list is then returned and printed.


##############

def count_ones(row):
    return row.count(1)

def find_max_ones(matrix):
    max_ones = 0
    max_row = -1

    for i, row in enumerate(matrix):
        ones_count = count_ones(row)
        if ones_count > max_ones:
            max_ones = ones_count
            max_row = i

    return max_row

matrix = []
print("Please enter a 4x4 matrix with only 1s and 0s (with spaces between each no.s):")
for _ in range(4):
    row = list(map(int, input().split()))
    matrix.append(row)

max_row = find_max_ones(matrix)

if max_row != -1:
    print(f"The row with the highest number of 1s is Row = {max_row+1}")
    print(f"Number of 1s: {matrix[max_row].count(1)}")
else:
    print("No row contains any 1s.")
####################################################
    def sum_middle_row_and_column(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    middle_row = rows // 2
    middle_col = cols // 2

    middle_value = matrix[middle_row][middle_col]

    row_sum = sum(matrix[middle_row])
    col_sum = sum(row[middle_col] for row in matrix)
    total_sum = row_sum + col_sum - middle_value
    return total_sum

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]

result = sum_middle_row_and_column(matrix)
print("Sum of middle row and middle column values (excluding middle value):", result)
      


      ############################################################################

# Sort the matrix without any inbuilt libraries of python

# After that, replace the left and right diagonals with 0's


def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

def sort_matrix(matrix):
    flattened_matrix = [item for sublist in matrix for item in sublist]
    flattened_matrix.sort()
    sorted_matrix = [flattened_matrix[i:i+len(matrix[0])] for i in range(0, len(flattened_matrix), len(matrix[0]))]

    return sorted_matrix

def replace_diagonals(matrix):
    size = len(matrix)
    for i in range(size):
        matrix[i][i] = 0
        matrix[i][size - i - 1] = 0

    return matrix

# Get the matrix from the user
matrix = get_matrix_from_user()

# Sort the matrix
sorted_matrix = sort_matrix(matrix)

# Print the sorted matrix
print("Sorted Matrix:")
print_matrix(sorted_matrix)

# Replace diagonals with 0's
modified_matrix = replace_diagonals(sorted_matrix)

# Print the modified matrix
print("\nMatrix with Diagonals Replaced:")
print_matrix(modified_matrix)




####################################################################


# Multiply 2 integers

# DO NOT USE multiplication, division, for loops, bitwise operators

# Can be done using Recursion


def multiplication(a, b):
    if b == 0:
        return 0
    return a + multiplication(a, b - 1)   # Recursion - funtion calling itself until the values are decremented to 0 
# Recursion is happening in the above line & 'multiplication(a, b-1)' causes recursion and until b = 0, recursion happens.
# This is resultion in 'repeated addition' which is the same as 'multiplication'

a = int(input("Enter 1st Integer : "))
b = int(input("Enter 2nd Integer : "))

result = multiplication(a,b)
print("Product: ", result)
