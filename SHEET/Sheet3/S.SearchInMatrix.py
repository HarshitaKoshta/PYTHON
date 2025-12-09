n,m = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

x = int(input())    

found = False
for i in arr:
    if x in i:
        found = True
        break


if found:
    print("will not take number")
else:
    print("will take number")
