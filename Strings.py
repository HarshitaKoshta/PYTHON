s = 'hellooo'
print(s)

s = "hellooo"
print(s)

s = '''hellooo'''
print(s)

print(s[0])
print(s[-1])
print(s[2:5])

# s[1] = 'k'     ==>error

del s  #del string
# print(s)

s1 = 'hello '
s2 = 'pihu'

print(s1+ s2)
print(s1*3)

count = 0
for l in 'hello world':
    if l=='l':
        count +=1
print(count,'letters found')        

print('l' in 'hello world')

print('org' in 'hello world')

print("pihu".lower(),"pihu".upper())

print("this will split all words in list".split())

print(''.join(['this ','will','join']))

print("Good morning".find('mo'))

s1 = "Bad morning"
s2 = s1.replace("Bad","Good")
print(s2)

rev =""
for i in st:
    rev = i +rev
    
if st==rev:
    print("palin")
else:
    print("not")

st = 'racecar race a krti h'
w = st.split()
w.sort()
for word in w:
    print(word)