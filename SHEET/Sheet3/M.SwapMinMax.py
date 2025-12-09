n = int(input())
a = list(map(int,input().split()))
mini= min(a)
maxi = max(a)
for i in range(n):
    if(a[i]==mini):
        a[i]=maxi
    elif(a[i]==maxi):
        a[i] = mini
print(*a)        