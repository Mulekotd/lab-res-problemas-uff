def insertion_sort(v: list[int]) -> None:
    n = len(v)

    for i in range(1, n):
        value = v[i]
        j = i
        while j > 0 and value < v[j - 1]:
            v[j] = v[j - 1]
            j -= 1
        v[j] = value

v = [10, 5, 3, 7]

insertion_sort(v)
