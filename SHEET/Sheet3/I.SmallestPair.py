t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = 993456

    for j in range(n):
        for k in range(j+1, n):
            val = a[j] + a[k] + (k - j)
            ans = min(ans, val)    

    print(ans)
