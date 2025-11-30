test = 1

while True:
    N = int(input())

    if N == 0:
        break

    possible = [set(range(10)) for _ in range(6)]

    for _ in range(N):
        data = input().split()
        
        nums = [int(x) for x in data[:10]]
        password = data[10:]

        letters = ['A', 'B', 'C', 'D', 'E']
        letter_map = {}

        for i, char in enumerate(letters):
            a = nums[2*i]
            b = nums[2*i + 1]
            letter_map[char] = {a, b}

        for i in range(6):
            letter = password[i]
            possible[i] &= letter_map[letter]

    decoded = [str(next(iter(s))) for s in possible]

    print(f"Teste {test}")
    print(" ".join(decoded), end=" \n\n")
    test += 1
