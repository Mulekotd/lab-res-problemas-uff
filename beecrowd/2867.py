import math

N = int(input())

for _ in range(N):
    n, m = map(int, input().split())
    digits = int(math.floor(m * math.log10(n))) + 1

    print(digits)
