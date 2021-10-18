import numpy as np

# outer product: where dot product is vTw, outer is vwT and produces an nxm matrix for size of the vectors, n,m
v = [0,2,3,6]
w = [5,3,7]

o = np.outer(v, w)
print(o)

# by hand
o2 = [[v[i] * w[j] for j in range(len(w))] for i in range(len(v))]
print(o2)

o3 = np.zeros((len(v), len(w)))
for i in range(len(v)):
    for j in range(len(w)):
        o3[i,j] = v[i]*w[j]
print(o3)
