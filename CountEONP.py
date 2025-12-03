n = int(input())    
a = list(map(int, input().split())) 

e = 0
odd =0
neg=0
pos=0

for i in a:
    if(i%2==0):
        e +=1
    if(i%2!=0):
        odd+=1    
    if(i<0):
        neg +=1
    if(i>0):
        pos +=1
    
print("Even:",e)
print("Odd:",odd)                    
print("Positive:",pos)                    
print("Negative:",neg)                    
