# tup = (3,5,3,6,4)
# t=(4,)
# print(type(tup))
# print(t)
# print(tup.count(3))


# grade = ("c","d","a","c")
# print(grade.count("c"))

# grade = ["c","d","a","c"]
# grade.sort()
# print(grade)


# t = (4,5,(3,4),[1,'raju',47,'abs'])
# print(type(t))
# print(t[3][1])

# t = (3,5,7,'pihu')
# print(t)

# t = ('pihu',)
# print(type(t))

# t= 'pihu','hsi'
# print(type(t))

# print(t[1])


# -----------------------slicing------------------------#


t = (2,5,6,3,2,4,2,[56,"hello",8])
# print(t[1:4])
# print(t[:-2])  #second lst tk print
# print(t[:])    #starting to end

# # t[3] = 'e'  #error not support assignment
# t[4][1] = '67'
# print(t)

# t = (1,2,3)+(4,5)
# print(t)

# t=(('pihu,')*4)
# print(t)

# del(t) #delete entire tup
# print(t)

print(t.count(2))

print(t.index(3))

print(1 in t)
print(5 in t)
print(len(t))

t = (2,5,6,3,2,4,2)
new_t = sorted(t)
print(new_t)
print(max(t))
print(min(t))
print(sum(t))
