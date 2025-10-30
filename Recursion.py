
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     return n*fact(n-1)
    

# print(fact(5))


# def fabo(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fabo(n-1) +fabo(n-2)   

# for i in range(10):
#     print(fabo(i), end=" ")


# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)

# print(sum(4))    


def print_rev(n):
    if n==6:
        return
    print_rev(n+1)
    print(n,end=' ')

print_rev(1)