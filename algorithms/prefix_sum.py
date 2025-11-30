def prefix_sum_1d(v: list[int]) -> list[int]:
    n = len(v)

    prefix = [0] * n
    prefix[0] = v[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + v[i]
    
    return prefix


def prefix_sum_2d(arr: list[list[int]]) -> list[list[list]]:
    L, C = len(arr), len(arr[0])
    prefix = [[0] * (L + 1) for _ in range(C + 1)]

    for i in range(L):
        for j in range(C):
            prefix[i][j] = arr[i][j] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
    
    prefix.pop(L)
    for line in prefix:
        line.pop(C)
    
    return prefix


array = [10, 20, 10, 5, 15]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(prefix_sum_1d(array)) # Output: [10, 30, 40, 45, 60]
print(prefix_sum_2d(matrix)) # Output: [[1, 3, 6, 10], [6, 14, 24, 36], [15, 33, 54, 78], [28, 60, 96, 136]]
