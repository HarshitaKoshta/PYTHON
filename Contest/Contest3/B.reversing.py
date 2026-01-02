a = int(input())
b = list(map(int,input().split()))

for i in range(a):
    if b[i]==0:
        b[:i] = reversed(b[:i])
print(*b)