n = int(input())
a = list(map(int, input().split()))

l, r = 0, n - 1
res = []

while l <= r:
    res.append(a[l])
    l += 1
    if l <= r:
        res.append(a[r])
        r -= 1

print(*res)
