t = 1

while True:
    N = int(input())
    if N == 0:
        break

    deposits = [list(map(int, input().split())) for _ in range(N)]

    acc_sum = []
    total_a = 0
    total_b = 0

    for a, b in deposits:
        total_a += a
        total_b += b
        acc_sum.append(total_a - total_b)

    print(f"Teste {t}")
    for value in acc_sum:
        print(value)
    print()

    t += 1
