a,b,c,d = map(int,input().split())
lst = []

lst.append(a+b-c)
lst.append(a+b*c)
lst.append(a-b+c)
lst.append(a-b*c)
lst.append(a*b-c)
lst.append(a*b+c)

if lst.__contains__(d):
    print("YES")
else:
    print("NO")    