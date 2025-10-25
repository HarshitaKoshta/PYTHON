coll = {2,4,46,5,3,2,"hellooo",4}
print(coll)
print(type(coll))
print(len(coll))

s = set() #empty set
s.add(3)
s.add(5)
s.add(7)
s.remove(5)
s.add((3,4,"hi"))
# s.add([3,4,"hi"]) #error
s.clear()
# s.pop()  -->remove random
print((s))

s1 = {3,5,6}
s2 = {2,3,4}
print(s1.union(s2))
print(s1.intersection(s2))

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture", "list of figures"]
}
print(dict)

subjects = {"python","java","c++","python","javascript","c++","c","java","python"}
print(len(subjects))