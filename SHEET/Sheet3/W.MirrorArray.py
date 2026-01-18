n, m = map(int, input().split())

for _ in range(n):
    row = list(map(int, input().split()))
    row.reverse()              
    print(*row)               