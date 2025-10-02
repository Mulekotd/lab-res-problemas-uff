x, y = map(int, input().split())

def format_num(n):
    if n > 0:
        return f"+{n}"
    elif n == 0:
        return f" {n}"
    else:
        return f"{n}"

x_numbers = [format_num(i) for i in range(-x, x + 1)]
y_numbers = [format_num(i) for i in range(y, -y - 1, -1)]

for yi, y_value in enumerate(y_numbers):
    row = []
    for x_value in x_numbers:
        row.append(f"({x_value},{y_value})")
    print(" ".join(row))
