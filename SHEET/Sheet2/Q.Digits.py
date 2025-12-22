n = int(input())

for i in range(n):
    k = input().strip()
    for i in range(len(k)-1, -1, -1):
        print(k[i],end=" ")
    print()    

    


    