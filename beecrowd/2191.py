count = 1

def best_period(matches):
    values = [x - y for x, y in matches]
    
    best_sum = float('-inf')
    best_i = best_j = -1
    
    current_sum = 0
    start = 0
    
    for i, v in enumerate(values):
        if current_sum + v < v:
            current_sum = v
            start = i
        else:
            current_sum += v
        
        if (current_sum > best_sum) or \
           (current_sum == best_sum and (i - start) > (best_j - best_i)):
            best_sum = current_sum
            best_i = start
            best_j = i
    
    if best_sum <= 0:
        return -1
    
    return best_i + 1, best_j + 1


while True:
    N = int(input())
    
    if N == 0:
        break
    
    matches = [tuple(map(int, input().split())) for _ in range(N)]
    result = best_period(matches)
    
    print(f"Teste {count}")
    if result == -1:
        print("nenhum")
    else:
        print(*result)
    print()
    
    count += 1
