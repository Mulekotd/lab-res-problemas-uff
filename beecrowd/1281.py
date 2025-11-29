N = int(input())

for _ in range(N):
    M = int(input())

    fruits = {}

    for _ in range(M):
        name, price = input().split()
        fruits[name] = float(price)

    Q = int(input())

    total_price = 0
    for _ in range(Q):
        name, quantity = input().split()
        fruit_price = fruits[name]
        total_price += (fruit_price * float(quantity))
    
    print(f"R$ {total_price:.2f}")
