def truncate_average(total, divider):
    if total >= 0:
        return total // divider
    else:
        return -((-total) // divider)

counter = 1

while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    if N == 0 or M == 0:
        print(f"Teste {counter}")
        print("0 0", end="\n\n")

        counter += 1
        continue

    test_cases = [int(input()) for _ in range(N)]
    avgs = []
    
    # Calculates the first window
    current_sum = sum(test_cases[:M])
    avgs.append(truncate_average(current_sum, M))
    
    # Sliding window
    for i in range(M, N):
        current_sum = (current_sum - test_cases[i - M]) + test_cases[i]
        avgs.append(truncate_average(current_sum, M))

    print(f"Teste {counter}")
    print(f"{min(avgs)} {max(avgs)}", end="\n\n")

    counter += 1
