alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

N = int(input())

for _ in range(N):
    chiper = input()
    displacement = int(input())

    phrase = []
    for char in chiper:
        idx = alphabet.index(char)
        phrase.append(alphabet[(idx - displacement) % 26])

    print("".join(phrase))
