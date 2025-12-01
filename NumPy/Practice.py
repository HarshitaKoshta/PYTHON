import numpy as np

a = np.arange(10)
print(a)

a = np.zeros((3,3))
print(a)

a = np.arange(10,50,5)
print(a)
print(a.shape)
print(a.dtype)
print(a.size)

a = np.random.rand(4,4)

print("Array", a)
print("Mean:", np.mean(a))
print("Sum:", np.sum(a))

a = np.array([2,45,2,54,2,3,66,56])
# a[a>50] = 50
# print(a)

print(a[len(a)-2:len(a)])

a = np.eye(5)
print(a)

print(a.flatten())