def winner(p1, p2):
    if p1 == p2:
        return "empate"
    elif (p1 == "tesoura" and p2 == "papel") or \
         (p1 == "papel" and p2 == "pedra") or \
         (p1 == "pedra" and p2 == "tesoura"):
        return "jogador 1"
    else:
        return "jogador 2"


test = 1

while True:
    n = int(input())
    
    if n == 0:
        break

    p1_plays = []
    while len(p1_plays) < n:
        p1_plays += input().split()

    p2_plays = []
    while len(p2_plays) < n:
        p2_plays += input().split()

    if test > 1:
        print()

    print(f"test {test}")

    for i in range(n):
        print(winner(p1_plays[i], p2_plays[i]))

    test += 1
