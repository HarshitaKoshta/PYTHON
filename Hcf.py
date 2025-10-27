def Calc_Hcf(a,b):
    while(b):
        a = b
        b = a % b
    return a    

h = Calc_Hcf(5,3)
print(h)