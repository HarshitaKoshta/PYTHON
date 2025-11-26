a,b = map(int,input().split())

for i in range(a,b+1):
    if i not in ('4','7'):
        print("-1")
    else:   
        print(i,end=" ")