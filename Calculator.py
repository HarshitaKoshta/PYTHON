print("select Option:")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. Division")

c = float(input("enter choice"))
a = float(input("enter no. 1st: "))
b = float( input("enter no. 2nd: "))

match c:
    case 1 : print(a+b)
    case 2 : print(a-b)        
    case 3 : print(a*b)
    case 4 : print(a//b)
           