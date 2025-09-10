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

# def factorial(n):
#     """calculate the factorial of n(n) 
#     n(int: a non negative number) 
#     return the value of n"""

#     return 1 if n==0 or n==1 else n*factorial(n-1)
# help(factorial)


# age = input("enter ur age:")
# print(type(age))

# age = int(age)
# print(type(age))

# values =[0," ",None,"hi",123]
# print("AND Operators:")
# for a in values:
#     for b in values:
#         print(f"{a!r} and {b!r}->{a and b!r}")
# print("\n OR operator")
# for a in values:
#     for b in values:
#         print(f"{a!r} and {b!r}->{a and b!r}")
# print("\n NOT operator")
# for a in values:
#         print(f"not:{a!r} -> {not a!r}")
# print("\n NOT operator")
         
# name = input("name:")
# print(f"hello, {name}")


# for i in range(1, 11):
#     print(f"2 x {i} = {2 * i}")


# isPrime = True

# for i in range(2, n):
#     if n % i == 0:
#         isPrime = False
#         break

# if isPrime:
#     print(" a prime number")
# else:
#     print("not a prime number")

# (isPrime)

# for i in range(0, n+1):
#     if(i%2==0):
#         print(i)

# for i in range(1, n+1,2):
#     print(i)

# n = 10

# sum=0
# for i in range(n):
#     sum+=  n

# print(sum)  
  

a = 0
b = 1
for i in range(20):
    print(a)
    temp = a + b
    a = b
    b = temp
    
