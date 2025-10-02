def vencedor(j1, j2):
    if j1 == j2:
        return "empate"
    elif (j1 == "tesoura" and j2 == "papel") or \
         (j1 == "papel" and j2 == "pedra") or \
         (j1 == "pedra" and j2 == "tesoura"):
        return "jogador 1"
    else:
        return "jogador 2"


teste = 1
while True:
    n = int(input())
    
    if n == 0:
        break

    jogadas_p1 = []
    while len(jogadas_p1) < n:
        jogadas_p1 += input().split()

    jogadas_p2 = []
    while len(jogadas_p2) < n:
        jogadas_p2 += input().split()

    if teste > 1:
        print()

    print(f"Teste {teste}")
    for i in range(n):
        print(vencedor(jogadas_p1[i], jogadas_p2[i]))

    teste += 1
