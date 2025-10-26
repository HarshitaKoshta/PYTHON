t = int(input())

for i in range(t):
    a, b = input().split()
    a = int(a)
    b = int(b)

    result = 1
    for j in range(b):
        result = result * a

    print(result % 10)
