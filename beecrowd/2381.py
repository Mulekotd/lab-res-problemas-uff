N, K = map(int, input().split())

students = []
for _ in range(N):
    student = input()
    students.append(student)

students.sort()
print(students[K-1])
