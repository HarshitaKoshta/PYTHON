# marks = [39,86.4,98,56.3]
# print(marks)
# print(type(marks))
# print(marks[2])
# print(marks[len(marks)-1])


#........List are mutable..........

# student = ["pihu",89,20,"jabalpur"]
# print(student)
# student[0] = "Harshita"
# print(student)
# print(student[0:3])

# student.append("English")
# print(student)
# list=[0,1,2,1,0]
#list.sort(reverse=True) #des sort
# list.reverse()
# list.insert(2,6)
# list.remove(2)    ------->>remove firts occurance
# list.pop(3)
# print(list)


# m1 = input("enter fav movie 1:")
# m2 = input("enter fav movie 2:")
# m3 = input("enter fav movie 3:")

# movies = []
# movies.append(m1)
# movies.append(m2)
# movies.append(m3)
# print(movies)


# nlist = list.copy()
# nlist.reverse()
# if(list == nlist):
#     print("palindrome")
# else:
#     print("not ")   


# l1 = [2,3,5,4]
# l2 = [9,2,3]
# del l1[1]          
# l1.extend(l2)
# print(l1)

# l = ['one','two','three']
# if 'two' in l:
#     print('present')

# if 'six' not in l:
#     print('not present')    

# l.reverse()    
# print(l)

# sorted_lst = sorted(l1)    #sorted fn sort in new list 
# print(sorted_lst)

# asc = sorted(l1,reverse = True)
# print(asc)

# listt = [5,4,2,4]
# listt.sort() 
# print(listt)


li = ['mango','apple','grapes','pineapple','banana']

for i in li:
    print(i.upper())
    
# num = [21,2,6,5,9]

# print(li[0])
# print(num[0])

# print(li[len(li)-2])
# print(len(li))

# li.append('berry')    
# print(li)

# for l in li:
#     print('I like:',l)

# li.insert(1,'orange')

# li.remove('apple')
# li.pop()
# print(li)

# b = [3,4]

# c = a+b
# print(c)

# if 'mango' in li:
#     print('yes')
# else:
#     print('not')    

# sum=0
# for i in a:
#     sum  +=i

# avg = sum/len(li)    
# print(sum) 
# print(avg)   

# max =0
# for j in a:
#     if(j>max):
#         max =j
# print(max)  
# a = [1,2,5,6,2,3,2,3]

# for i in a:
#     f=0
#     for j in a:
#         if(i==j):
#             f=f+1
#     print(i,":",f)

# print(a.count(2))
# i=0
# while i< len(lst):
#     if(i == 'y'):
#         print(i)
#     i=i+1   

lst = ['x', 'y', 'z', 'x', 'y']

# for i in range(len(lst)):
#     if lst[i] == 'y':
#         print(i)
#         break

# print(lst.index('y'))

# for i in range(len(li),-1):
#     print(i)

# lst.reverse()
# print(lst)

# print(lst[:]) =>print all num

# print(lst[0:3])

print(lst[2,4])