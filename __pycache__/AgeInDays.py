x = int(input())
if(x<365):
    print("0 years")
if(x>=365):
    y = x//365
    x=x%365
    print(y,"years")
if(x<30):
    print("0 months")    
if(x>=30):
    k = x//30
    x = x%30
    print(k,"months")
if(x>=0):
    print(x,"days")
