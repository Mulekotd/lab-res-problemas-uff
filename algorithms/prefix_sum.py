from typing import Union

def prefix_sum(v: list[int]) -> list[int]:
    rows = len(v)

    prefix = [0] * rows
    prefix[0] = v[0]

    for i in range(1, rows):
        prefix[i] = prefix[i - 1] + v[i]

    return prefix


def prefix_sum_2D(matrix: list[list[int]], queries: list[list[int]] | None = None) -> Union[list[list[int]], list[int]]:
    rows = len(matrix)
    cols = len(matrix[0])

    if queries is None:
        prefix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                # Start with original value
                prefix[i][j] = matrix[i][j]

                # Add value from top cell if it exists
                if i > 0:
                    prefix[i][j] += prefix[i - 1][j]

                # Add value from left cell if it exists
                if j > 0:
                    prefix[i][j] += prefix[i][j - 1]

                # Subtract overlap from top-left diagonal if it exists
                if i > 0 and j > 0:
                    prefix[i][j] -= prefix[i - 1][j - 1]
        
        return prefix

    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

    # Build prefix matrix with 1-based indexing
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            prefix[i][j] = matrix[i - 1][j - 1] \
                        + prefix[i - 1][j] \
                        + prefix[i][j - 1] \
                        - prefix[i - 1][j - 1]

    result = []

    # Process each query using inclusion-exclusion
    for query in queries:
        top_row = query[0] + 1
        left_col = query[1] + 1
        bottom_row = query[2] + 1
        right_col = query[3] + 1

        # Get total area from (top_row, left_row) to (bottom_row, right_col)
        total = prefix[bottom_row][right_col]

        # Subtract area above the submatrix
        top = prefix[top_row - 1][right_col]

        # Subtract area to the left of the submatrix
        left = prefix[bottom_row][left_col - 1]

        # Add back the overlapping top-left area, which was subtracted twice
        overlap = prefix[top_row - 1][left_col - 1]

        # Final submatrix sum using inclusion-exclusion
        result.append(total - top - left + overlap)

    return result


array = [10, 20, 10, 5, 15]
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
queries = [[1, 1, 2, 2]]

print(prefix_sum(array)) # Output: [10, 30, 40, 45, 60]
print(prefix_sum_2D(matrix)) # Output: [[1, 3, 6, 10], [6, 14, 24, 36], [15, 33, 54, 78], [28, 60, 96, 136]]
print(prefix_sum_2D(matrix, queries)) # Output: [34]
