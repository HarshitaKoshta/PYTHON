n = int(input())
a = list(map(int, input().split()))

# Pattern 1: + - + - ...
ops1 = 0
# Pattern 2: - + - + ...
ops2 = 0

for i in range(n):
    if i % 2 == 0:
        # index even
        if a[i] < 0:
            ops1 += 1   
        if a[i] > 0:
            ops2 += 1   
    else:
        # index odd
        if a[i] > 0:
            ops1 += 1   
        if a[i] < 0:
            ops2 += 1

print(min(ops1, ops2))
