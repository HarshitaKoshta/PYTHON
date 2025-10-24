# marks = [39,86.4,98,56.3]
# print(marks)
# print(type(marks))
# print(marks[2])
# print(marks[len(marks)-1])

#........List are mutable..........

student = ["pihu",89,20,"jabalpur"]
# print(student)
# student[0] = "Harshita"
# print(student)
# print(student[0:3])

student.append("English")
# print(student)
list=[0,1,2,1,0]
#list.sort(reverse=True) #des sort
# list.reverse()
# list.insert(2,6)
# list.remove(2)
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


nlist = list.copy()
nlist.reverse()
if(list == nlist):
    print("palindrome")
else:
    print("not ")   
