k,s = map(int,input().split())
count = 0
for i in range(k+1):
    for j in range(k+1):
        m = s-i-j
        if 0<=m<=k:
            count +=1
    
print(count)
