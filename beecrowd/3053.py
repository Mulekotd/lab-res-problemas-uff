N = int(input().strip())
coin = input().strip()

for _ in range(N):
    op = int(input().strip())

    if op == 1:
        # A <-> B
        if coin == 'A': coin = 'B'
        elif coin == 'B': coin = 'A'
    elif op == 2:
        # B <-> C
        if coin == 'B': coin = 'C'
        elif coin == 'C': coin = 'B'
    else:
        # A <-> C
        if coin == 'A': coin = 'C'
        elif coin == 'C': coin = 'A'

print(coin)
