v = [10, 5, 3, 7, 0, -5, -3, -7, -10]


def insertion_sort(v: list[int]) -> None:
    n = len(v)

    for i in range(1, n):
        value = v[i]
        j = i
        while j > 0 and value < v[j - 1]:
            v[j] = v[j - 1]
            j -= 1
        v[j] = value


def bubble_sort(v: list[int]) -> None:
    n = len(v)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]


# insertion_sort(v)
# TODO: selection_sort(v)
bubble_sort(v)
# TODO: merge_sort(v)
# TODO: quick_sort(v)
# TODO: counting_sort(v)

print(v)
