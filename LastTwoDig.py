a,b,c,d = map(int,input().split())

c = a*b*c*d
c= c%100

if c < 10:
    print("0" + str(c))
else:
    print(c)