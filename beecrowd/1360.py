values = ['1','2','3','4','5','6','7','8','9','T','J','Q','K']
suits  = {'H':0, 'C':1, 'D':2, 'S':3}

# Mapa de permutações
perm_to_num = {(0,1,2): 1, (0,2,1): 2, (1,0,2): 3, (1,2,0): 4, (2,0,1): 5, (2,1,0): 6}

def card_key(card):
    return (suits[card[1]], values.index(card[0]))

def decode_hidden(cards):
    base = cards[0]
    z = cards[1:]  # z1, z2, z3
 
    # Obtem a ordem crescente segundo a ordem completa (naipe, valor)
    order = sorted(range(3), key=lambda i: card_key(z[i]))
    
    # Ranks: para cada posição original (z1, z2, z3) qual é a sua posição entre (menor,medio,maior)
    ranks = tuple(order.index(i) for i in range(3))
    k = perm_to_num[ranks] # Número entre 1 e 6

    base_val_idx = values.index(base[0])
    hidden_val_idx = (base_val_idx + k) % 13

    return values[hidden_val_idx] + base[1]

n = int(input())

for _ in range(n):
    print(decode_hidden(input().split()))
