def ceil(x):
    return int(x) + (x % 1 > 0)

v, n = map(int, input().split())
total = v * n
result = [ceil(total * i / 10) for i in range(1, 10)]

print(*result)
