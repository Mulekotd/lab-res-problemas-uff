N = int(input())

for _ in range(N):
    M = int(input())

    fruits = {}
    for _ in range(M):
        name, price_kg = input().split()
        fruits[name] = float(price_kg)

    Q = int(input())

    total = 0
    for _ in range(Q):
        name, quantity = input().split()
        fruit_price = fruits[name]
        total += (fruit_price * int(quantity))
    
    print(f"R$ {total:.2f}")
