n = int(input())
a = list(map(int,input().split()))
mini=100000
for i in range(n):
    mini = min(a[i],mini)
    # print(mini)
c = a.count(mini)
if(c%2==0):
    print("Unlucky")
else:
    print("Lucky")    