while True:
    N, C, K = map(int, input().split())
    
    if N == 0 and C == 0 and K == 0:
        break

    frequency = [0] * (K + 1)

    for _ in range(N):
        nums = list(map(int, input().split()))
        for x in nums:
            frequency[x] += 1

    minimum = min(frequency[1:])

    result = []
    for i in range(1, K + 1):
        if frequency[i] == minimum:
            result.append(i)

    print(" ".join(map(str, result)))
