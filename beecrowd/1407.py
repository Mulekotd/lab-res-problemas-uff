while True:
    n, c, k = map(int, input().split())
    
    if n == 0 and c == 0 and k == 0:
        break

    freq = [0] * (k + 1)

    for _ in range(n):
        nums = list(map(int, input().split()))
        for x in nums:
            freq[x] += 1

    minimum = min(freq[1:])

    result = []
    for i in range(1, k + 1):
        if freq[i] == minimum:
            result.append(i)

    print(" ".join(map(str, result)))
