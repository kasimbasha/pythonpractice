import numpy as np
from numpy.random import rand

np.set_printoptions(precision=2)

aa = np.array([[2,4,6],[1,3,5],[10,20,30]])
bb = np.array([[0,2,7],[1,3,5],[10,20,30]])

print(aa*bb)
print(np.dot(aa,bb)) # using np dot function