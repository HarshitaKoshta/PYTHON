t = int(input())  

for _ in range(t):
    a,b = map(int, input().split())

    a = a % 10   
    result = 1

    for i in range(b):
        result = (result * a) % 10  

    print(result)
