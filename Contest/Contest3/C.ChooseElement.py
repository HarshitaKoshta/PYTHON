n,k = map(int,input().split())

b = list(map(int,input().split()))
b.sort(reverse=True)

s=0
count=0
for i in b:
    if i>0 and count<k:
        s += i
        count += 1

print(s)        

    
    

 