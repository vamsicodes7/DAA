def find_triplets(arr, target_sum):
    n = len(arr)

    arr.sort()

    triplets = []


    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets


A = [1, 2, 3, 4, 5]
target_sum = 9
result = find_triplets(A, target_sum)

if result:
    print(f"Triplets with sum {target_sum}: {result}")
else:
    print(f"No triplets found with sum {target_sum}")
