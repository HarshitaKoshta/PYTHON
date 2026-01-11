def nTimes(n, c):
    # print character c, n times separated by space
    print((c + " ") * n)


T = int(input())

for _ in range(T):
    n, c = input().split()
    n = int(n)
    nTimes(n, c)
