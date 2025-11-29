n = int(input())
a = list(map(int,input().split()))
k = a[0]
pos= 1
for i in range(1,n):
    if(a[i]<k):
        k=a[i]
        pos=i+1

print(k,pos)
