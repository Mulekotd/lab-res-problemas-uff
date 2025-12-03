N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

sum_set = set()

principal_diagonal = 0
secondary_diagonal = 0

for i in range(N):
    row_sum = 0
    col_sum = 0

    for j in range(N):
        row_sum += matrix[i][j]
        col_sum += matrix[j][i]

    # Adiciona linha e coluna
    sum_set.add(row_sum)
    sum_set.add(col_sum)

    # Acumula diagonais
    principal_diagonal += matrix[i][i]
    secondary_diagonal += matrix[i][N - 1 - i]

# Adiciona diagonais
sum_set.add(principal_diagonal)
sum_set.add(secondary_diagonal)

print(-1) if len(sum_set) > 1 else print(*sum_set)
