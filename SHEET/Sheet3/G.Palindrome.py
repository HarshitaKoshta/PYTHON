n = int(input())
a = list(map(int,input().split()))
s=0
e = n-1
found = True
while(s<e):
    if(a[s]==a[e]):
        s+=1
        e-=1
        if(s==e):
            break
    else:
        found = False    
        break

if(found):
    print("YES")
else:
    print("NO")    
   