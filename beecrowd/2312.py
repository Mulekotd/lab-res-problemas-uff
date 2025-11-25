from functools import cmp_to_key


def cmp_medals(q1, q2):
    if q1[1] > q2[1]: return -1
    elif q1[1] < q2[1]: return 1
    elif q1[2] > q2[2]: return -1
    elif q1[2] < q2[2]: return 1
    elif q1[3] > q2[3]: return -1
    elif q1[3] < q2[3]: return 1
    elif q1[0] < q2[0]: return -1
    elif q1[0] > q2[0]: return 1
    
    return 0


N = int(input())
countries = []
for _ in range(N):
    C = input().split()
    C[1], C[2], C[3] = int(C[1]), int(C[2]), int(C[3])
    countries.append(tuple(C))

countries.sort(key=cmp_to_key(cmp_medals))

for medal in countries:
    print(*medal)
