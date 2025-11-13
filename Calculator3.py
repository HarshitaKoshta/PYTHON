import math

a,s,b = input().strip()
a = int(a)
b = int(b)
if(s=='+'):
    r = a+b
elif(s == '*'):
    r=a*b
elif(s == '-'):
    r=a-b    
elif(s=='/'):
    r =int(a)//int(b) 
     

print(r)

