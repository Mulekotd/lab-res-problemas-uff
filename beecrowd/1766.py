T = int(input())

for i in range(T):
    N, M = map(int, input().split())

    reindeers = []
    for _ in range(N):
        R = input().split()
        R[1], R[2], R[3] = int(R[1]), int(R[2]), float(R[3])
        reindeers.append(tuple(R))
    
    reindeers.sort(key=lambda x: (-x[1], x[2], x[3], x[0]))

    print(f"CENARIO {{{i+1}}}")
    for index, reindeer in enumerate(reindeers[:M], 1):
        print(f"{index} - {reindeer[0]}")
