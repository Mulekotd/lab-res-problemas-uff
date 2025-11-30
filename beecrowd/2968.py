def ceil(x):
    return int(x) + (x % 1 > 0)

V, N = map(int, input().split())

total = V * N
result = [ceil(total * i / 10) for i in range(1, 10)]

print(*result)
