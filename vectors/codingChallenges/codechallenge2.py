import numpy as np

# is the dot product commutative?
# a'b == b'a  -> a transpose b == b transpose a  -> a dot b == b dot a

# 1. generate two random 100 element row vectors and compute a'b and b'a
# 2. do the same with two 2-element(int) vectors for ease of checking

a = np.random.randn(100)
b = np.random.randn(100)
print(a)
print(b)
print(np.dot(a, b))
print(np.dot(b, a))

c = np.random.rand(2)
d = np.random.rand(2)
print(c, d)
print(np.dot(c, d))
print(np.dot(d, c))
