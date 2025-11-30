N = int(input())


def reversed_sort(v: list[int]):
    n = len(v)
    aux = v.copy()

    for i in range(n):
        for j in range(n - i - 1):
            if aux[j] < aux[j+1]:
                aux[j+1], aux[j] = aux[j], aux[j+1]
    
    return aux


for _ in range(N):
    M = int(input())
    queue = list(map(int, input().split()))
    displacements = reversed_sort(queue)

    counter = 0
    for i in range(M):
        if queue[i] == displacements[i]:
            counter += 1
    
    print(counter)
