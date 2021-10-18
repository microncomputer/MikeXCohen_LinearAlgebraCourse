import numpy as np

# test whether dot product sign is invariant to scalar multiplication
# generate two vectors (R3)
# generate two scalars
# compute dot product between the vectors
# compute dot product between the scaled vectors

v1 = np.random.randn(3)
v2 = np.random.randn(3)
s1 = np.random.randint(-2000, 2000)
s2 = np.random.randint(-2000, 2000)

dot1 = np.dot(v1, v2)
dot2 = np.dot(s1*v1, s2*v2)

print("original dot product of the two vectors: ", dot1)
print("dot product of the two independently scaled vectors: ", dot2)
