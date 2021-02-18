import numpy as np
from numpy.random import rand

np.set_printoptions(precision=2)

a = np.array([1,2,3,4,5,6])
b = np.array([[10,20,30],[40,50,60]])
np.random.seed(25)
c = 36 * np.random.rand(6)
d = np.arange(1,35)

print(a)
print(b)
print(c)
print(d)

print(a*10)
print(c+a)