# x = 10
# y = x
# print(id(x))
# print(id(y))

# immutable --- cannot change the object (any change makes a new object)
# mutable ----- object can change without creating a new one

# a = "hy"ṇ
# print(id(a))
# a = a+ "there"ṇ
# print(id(a))

# list = [1,2,3]  #muttable
# print(id(list))
# list.append(6)
# print(id(list))

# a = [1,2,3]
# b=a
# print(id(a))
# b =a.copy()
# b.append(4)
# print(a)


# print(type(b)) 

# a =29
# print(type(a))

# b = "this is variable"
# print(type(b))

# def func():
#     pass
# print(type(func))

# class demo:
#     pass
# print(type(demo))

#####in python each and every thing is object

# """Doc string""" doc string defines in """ commas
# through help function we can print doc string

def factorial(n):
    """calculate the factorial of n(n) 
    n(int: a non negative number) 
    return the value of n"""

    return 1 if n==0 or n==1 else n*factorial(n-1)
help(factorial)


