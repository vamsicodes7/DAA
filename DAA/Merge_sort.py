def merge_sort(input_list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2
    left_half = input_list[:mid]
    right_half = input_list[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a space: ")
    unsorted_numbers = [int(item) for item in user_input.split()]
    print("Original List: ", unsorted_numbers)
    print("Sorted List: ", merge_sort(unsorted_numbers))