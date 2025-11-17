def max_subarray_sum(arr: list[int]) -> int:
    max_ending = arr[0]
    result = arr[0]

    for i in range(1, len(arr)):
        max_ending = max(arr[i], max_ending + arr[i])
        result = max(result, max_ending)

    return result

print(max_subarray_sum([-2, -4]))
print(max_subarray_sum([2, 3, -8, 7, -1, 2, 3]))
print(max_subarray_sum([5, 4, 1, 7, 8]))
