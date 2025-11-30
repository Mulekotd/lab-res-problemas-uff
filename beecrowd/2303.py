L, C, M, N = map(int, input().split())
matrix = [[0] * (C + 1)]

for _ in range(L):
    matrix.append([0] + list(map(int, input().split())))

for line in range(1, L + 1):
    total = 0
    
    for col in range(1, C + 1):
        total += matrix[line][col]
        matrix[line][col] = total + matrix[line-1][col]

max_daisy = 0
for i in range(M, L + 1, M):
    for j in range(N, C + 1, N):
        partial = matrix[i][j] + matrix[i-M][j-N] - matrix[i-M][j] - matrix[i][j-N]
        
        if partial > max_daisy:
            max_daisy = partial

print(max_daisy)
