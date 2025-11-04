while True:
    n = int(input())

    if n == 0:
        break

    results = map(int, input().split())

    mary_acc = 0
    john_acc = 0

    for element in results:
        if element == 0:
            mary_acc += 1
        else:
            john_acc += 1
    
    print(f"Mary won {mary_acc} times and John won {john_acc} times")
