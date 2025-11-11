s = {1,2,3,7,3,7}
# print(type(s))
# print(s)

# l=set([3,5,2,3])
# print(l)

#initialize a set
# s =set()
# print(type(s))
# print(s[3])
# s.add(6)     add in set

# s.update([3,4,2])  #=>add multiple value
# print(s)

# s.update([8,9],{30,7,6})
# # print(s)

# # s.discard(2)
# s.pop()
# s.clear()
# print(s)


# s1 = {4,1,7,2,4}
# s2 = {1,7}
# print(s1|s2) 
# print(s1.union(s2))

# print(s1 & s2)
# print(s1.intersection(s2))

# print(s1-s2)  #difference
# print(s1.difference(s2))

# print(s1^s2)
# print(s1.symmetric_difference(s2))

# print(s2.issubset(s1))
# print(s1.issubset(s2))

# s1 =frozenset([2,3,4,5])
# s2 = frozenset([2,3,7,9])  #=>do not change
# s1.add(2) =>error
# print(s1 | s2)

lst = ['hello', 'hii', 'hmm', 'harshita']

common = set(lst[0])
print(common)

for i in range(1,len(lst)-1):
    common = common.intersection(set(i))

print("Common characters:", common)
