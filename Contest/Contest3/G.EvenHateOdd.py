t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    even = 0
    odd = 0
    
    for x in arr:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    
    if n % 2 != 0:
        print(-1)
    else:
        print(abs(even - odd) // 2)
