n = int(input())

for i in range(n):
    x = int(input())
    y = int(input())
    a = x
    b = y

    while b != 0:
        temp = b
        b = a % b
        a = temp
    gcd = a
    lcm = (x * y) // gcd
    print(gcd, lcm)
