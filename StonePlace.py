n= int(input("Enter number of stones: "))

i = 1 
while n> 0:
    if n<= i:
        print("Ramesh")
        break
    n-= i
    if n<= 2*i:
        print("Suresh")
        break
    n-=2*i
    
    i += 1  