# x = 10
# y = x
# print(id(x))
# print(id(y))

# immutable --- cannot change the object (any change makes a new object)
# mutable ----- object can change without creating a new one

# a = "hy"
# print(id(a))
# a = a+ "there"
# print(id(a))

# list = [1,2,3]  #muttable
# print(id(list))
# list.append(6)
# print(id(list))

a = [1,2,3]
b=a
print(id(a))
b =a.copy()
b.append(4)
print(a)