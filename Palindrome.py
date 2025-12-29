n  = int(input())
new =n
res =0  
while(n>0):
    d = n%10
    res = res*10+d  
    n = n//10
print(res)   
if(new== res):
    print("YES")    
else:
    print("NO")    