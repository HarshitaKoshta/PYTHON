t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    for j in range(n):
        maxi=0
        for k in range(j):
            maxi = max(a[k],maxi)
        print(maxi,end=" ")

