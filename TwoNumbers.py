import math
A,B = map(int,input().split())
f = math.floor(A/B)
c = math.ceil(A/B)
r = math.floor(A/B + 0.5)

print("floor",A ,"/",B,"=",f)
print("ceil",A ,"/",B,"=",c)
print("round",A ,"/",B,"=",r)


