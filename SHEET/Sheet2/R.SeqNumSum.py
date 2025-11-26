while True:
    N,M = map(int, input().split())

    if N <= 0 or M <= 0:
        break
    start = min(N, M)
    end = max(N, M)
    total = 0

    for x in range(start, end + 1):
        print(x, end=" ")
        total += x

    print("sum =", end="")   
    print(total)