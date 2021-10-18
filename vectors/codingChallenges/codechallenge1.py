import numpy as np

# create 2 4x6 matrices of random numbers
# use a for loop to compute dot products between corresponding columns

A = [np.random.randn(4) for i in range(6)]
B = [np.random.randn(4) for i in range(6)]
print(A)
print(B)

columndots = [np.dot(A[i], B[i]) for i in range(6)]
print(columndots)
