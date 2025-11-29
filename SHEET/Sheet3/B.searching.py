n = int(input())
a = list(map(int,input().split()))
k = int(input())

found = False
for i in range(n):
    if a[i]==k:
        print(i)
        found = True
        break

if not found:
    print(-1)
