dic = {}
dic = {1:'abc', 2:'xyz'}

print(dic)

dic = {'name': 'pihu',1:['abc','ds']}
print(dic['name'])   #it can be accessed by value
dic = dict()
dic = dict([(1,'acd'),(2,'ewcd')])
# print(dic[3])  error
print(dic.get(2))
print(dic.get(3))    #it not give error only give none

dic['name'] = 'harshita'
print(dic)
dic['lstname'] = 'koshta'
print(dic)

print(dic.pop(2))
dic.popitem()
print(dic)

sq = {2:4,3:9,4:12}

# del sq[2]
# sq.clear()
# del sq

d=sq.copy()
print(d)

sub = {}.fromkeys(['math','english','hindi'],0) 
print(sub)

sub={2:3,4:6,8:8}
print(sub.items())  #return a new view of dic items(key,value)

print(sub.values())
print(sub.keys())
# print(dir(sub))  #print all methods

# for p in sub.items():
#     print(p)

# new = {k:v for k,v in sub.items() if v>3}
d = {k *'c':v *2 for k, v in d.items() if v>2}
print(d)