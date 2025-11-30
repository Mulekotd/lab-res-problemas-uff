import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    digits = int(math.floor(M * math.log10(N))) + 1

    print(digits)
