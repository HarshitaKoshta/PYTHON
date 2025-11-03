
# def palin(n):
#     s =0
#     y=n
#     while(n>0):
#         d = n%10
#         s = s*10+d
#         n = n//10
#     if(s==y):
#         print("palin")
#     else:
#         print("not")
# palin(121)    


double = lambda s: s == s[::-1]
print(double("123"))

