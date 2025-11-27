import numpy as np


a = np.array([0,1,2,3])
print(a)

print(np.arange(10))


l = range(1000)
print(%timeit (i**2 for i in l))
