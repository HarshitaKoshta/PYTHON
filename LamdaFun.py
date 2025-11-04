# double = lambda x,y: x+y

# print(double(5,6))


doubl = lambda x: 0 if x == 0 else (x%10)+doubl(x//10)

print(doubl(323))   

