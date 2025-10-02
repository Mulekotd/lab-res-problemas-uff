num = int(input())
intersections = set(map(int, input().split()))

for _ in range(num - 1):
    elements = set(map(int, input().split()))
    intersections &= elements

if intersections:
    print(*intersections)
else:
    print("vazio")
