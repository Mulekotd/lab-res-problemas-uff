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
    N = int(input())
    
    if N == 0:
        break

    p1_plays = []
    while len(p1_plays) < N:
        p1_plays += input().split()

    p2_plays = []
    while len(p2_plays) < N:
        p2_plays += input().split()

    if test > 1:
        print()

    print(f"test {test}")

    for i in range(N):
        print(winner(p1_plays[i], p2_plays[i]))

    test += 1
