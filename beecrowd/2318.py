from fractions import Fraction

def solve_magic_square(matrix):
    # Map zero cells to variables
    var_index = {}  # (i,j) -> idx
    idx = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                var_index[(i,j)] = idx
                idx += 1

    if idx == 0:
        return matrix

    M_idx = idx
    n_vars = idx + 1

    # Build equations: each row, col, diagonal -> sum_of_elements - M = 0
    equations = []  # each is (coeffs list length n_vars, rhs)
    def add_equation(cells):
        coeffs = [Fraction(0) for _ in range(n_vars)]
        const = Fraction(0)

        for (i,j) in cells:
            if matrix[i][j] == 0:
                coeffs[var_index[(i,j)]] += Fraction(1)
            else:
                const += Fraction(matrix[i][j])

        # Coefficient for M is -1 because sum(cells) - M = 0
        coeffs[M_idx] += Fraction(-1)
        rhs = -const
        equations.append((coeffs, rhs))

    # 3 rows
    for i in range(3):
        add_equation([(i,0),(i,1),(i,2)])

    # 3 columns
    for j in range(3):
        add_equation([(0,j),(1,j),(2,j)])

    # main diagonal
    add_equation([(0,0),(1,1),(2,2)])
    # secondary diagonal
    add_equation([(0,2),(1,1),(2,0)])

    # Build augmented matrix
    A = [row[0][:] + [row[1]] for row in equations]

    # Gaussian elimination
    m = len(A)
    n = n_vars

    row = 0
    for col in range(n):
        pivot = None
        for r in range(row, m):
            if A[r][col] != 0:
                pivot = r
                break

        if pivot is None:
            continue

        if pivot != row:
            A[row], A[pivot] = A[pivot], A[row]

        fac = A[row][col]
        A[row] = [v / fac for v in A[row]]

        for r in range(m):
            if r != row and A[r][col] != 0:
                factor = A[r][col]
                A[r] = [A[r][c] - factor * A[row][c] for c in range(n+1)]
    
        row += 1
        if row == m:
            break

    # Extract solution
    solution = [Fraction(0) for _ in range(n)]
    determined = [False] * n

    for r in range(m):
        first = None

        for c in range(n):
            if A[r][c] != 0:
                first = c
                break
        
        if first is None:
            continue

        solution[first] = A[r][n]
        determined[first] = True

    # Convert Fractions to ints
    int_sol = [int(sol_i) for sol_i in solution]

    # Fill matrix
    for (i,j), vidx in var_index.items():
        matrix[i][j] = int_sol[vidx]

    return matrix


matrix = [list(map(int, input().split())) for _ in range(3)]
matrix = solve_magic_square(matrix)

for row in matrix:
    print(*row)
