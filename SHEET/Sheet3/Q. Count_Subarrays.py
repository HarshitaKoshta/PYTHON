t = int(input())
for c in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    
    count = 0
    
    for i in range(n):
        for j in range(i,n):
            dec = True
            for k in range(i,j):
                if arr[k]>arr[k+1]:
                    dec = False
                    break
            if dec:
                count += 1
    print(count)
