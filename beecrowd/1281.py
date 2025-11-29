N = int(input())

for _ in range(N):
    M = int(input())

    fruits = {}

    for _ in range(M):
        fruit_name, price_kg = input().split()
        fruits[fruit_name] = float(price_kg)

    Q = int(input())

    total_price = 0
    for _ in range(Q):
        fruit_name, quantity = input().split()
        fruit_price = fruits[fruit_name]
        total_price += (fruit_price * int(quantity))
    
    print(f"R$ {total_price:.2f}")
