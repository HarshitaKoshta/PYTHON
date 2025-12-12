n = int(input())

for i in range(n):
    k = int(input())
    fact = 1
    for j in range(1,k+1):
        fact *= j
    print(fact)
