from functools import cmp_to_key


def cmp_reindeers(d1, d2):
    if d1[1] > d2[1]: return -1
    elif d1[1] < d2[1]: return 1
    elif d1[2] < d2[2]: return -1
    elif d1[2] > d2[2]: return 1
    elif d1[3] < d2[3]: return -1
    elif d1[3] > d2[3]: return 1
    elif d1[0] < d2[0]: return -1
    elif d1[0] > d2[0]: return 1
    
    return 0


T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    reindeers = []
    for _ in range(N):
        R = input().split()
        R[1], R[2], R[3] = int(R[1]), int(R[2]), float(R[3])
        reindeers.append(tuple(R))
    
    reindeers.sort(key=cmp_to_key(cmp_reindeers))

    print(f"CENARIO {{{i+1}}}")
    for index, reindeer in enumerate(reindeers[:M], 1):
        print(f"{index} - {reindeer[0]}")
