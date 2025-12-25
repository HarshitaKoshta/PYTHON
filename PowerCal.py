n = int(input())

for i in range(n):
    a,b = map(int,input().split())
    a= a%10
    res=1
    for j in range(b):
        res = res*a
    res=res%10
    print(res)