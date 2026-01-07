n = int(input())
arr = list(map(int, input().split()))

max_count = 0

for x in arr:
    count = 0
    while x % 2 == 0:
        x //= 2
        count += 1
    max_count = max(max_count, count)

print(max_count)
