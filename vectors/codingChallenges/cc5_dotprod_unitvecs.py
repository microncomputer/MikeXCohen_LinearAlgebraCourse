import numpy as np

# create two random-int vectors (R4)
# compute the lengths of each vector and the magnitude of dot product
# normalize the vectors
# compute magnitude of unit vector dot product

v1 = np.random.randint(10000, size=4)
v2 = np.random.randint(10000, size=4)
print("v1: ", v1)
print("v2: ", v2)

l1 = np.sqrt(np.dot(v1,v1))
l2 = np.sqrt(np.dot(v2,v2))
print("v1 length: ", l1)
print("v2 length: ", l2)

dotmag = np.abs(np.dot(v1, v2))
print("mag of dot product v1Tv2: ", dotmag)

mu1 = 1/l1
mu2 = 1/l2
v1n = mu1*v1
v2n = mu2*v2

dotmagn = abs(np.dot(v1n, v2n))
print("mag of dot product of normalized vectors: ", dotmagn)
