N, M = map(int, input().split())
matrix = [[0] * (M + 1)]

for _ in range(N):
    matrix.append([0] + list(map(int, input().split())))

for row in range(1, N + 1):
    row_accumulator = 0

    for col in range(1, M + 1):
        row_accumulator += matrix[row][col]
        matrix[row][col] = row_accumulator + matrix[row - 1][col]

# Cálculo das somas de linhas e colunas
prefix_sums = []

for row in range(1, N + 1):
    if row == 1:
        row_sum = matrix[row][M]
    else:
        row_sum = matrix[row][M] - matrix[row - 1][M]

    prefix_sums.append(row_sum)

for col in range(1, M + 1):
    if col == 1:
        col_sum = matrix[N][col]
    else:
        col_sum = matrix[N][col] - matrix[N][col - 1]

    prefix_sums.append(col_sum)

print(max(prefix_sums))
