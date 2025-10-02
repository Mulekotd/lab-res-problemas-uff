n = int(input())
pascals_triangle = []

for i in range(n):
    if i == 0:
        pascals_triangle.append([1])
    else:
        prev = pascals_triangle[-1]
        new_row = [1]

        for j in range(len(prev) - 1):            
            new_row.append(prev[j] + prev[j+1])
        
        new_row.append(1)
        pascals_triangle.append(new_row)

for line in pascals_triangle:
    print(*line)
