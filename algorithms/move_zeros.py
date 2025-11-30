def move_zeros(v):
    n = len(v)

    non_zero = []
    for i in range(n):
        if v[i] != 0:
            non_zero.append(v[i])

    m = len(non_zero)

    i = 0
    while i < n:
        for num in non_zero:
            v[i] = num
            i += 1
        
        for _ in range(m - 1, n - 1):
            v[i] = 0
            i += 1

    return v


print(move_zeros([0, 1, 3, 0, 12, 0, 2])) # Output: [1, 3, 12, 2, 0, 0, 0]
print(move_zeros([0, 0, 0, 0, 1])) # Output: [1, 0, 0, 0, 0]
