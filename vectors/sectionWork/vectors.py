import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v2 = [3, -2]
v3 = [4, -3, 2]

# row to column or vice verca:
v3t = np.transpose(v3)

# plot
plt.plot([0, v2[0]], [0, v2[1]])
plt.axis('equal')
plt.plot([-4, 4], [0, 0], 'k--')
plt.plot([0, 0], [-4, 4], 'k--')
plt.grid()
plt.axis((-4, 4, -4, 4))
plt.show()

# plot 3d vector
fig = plt.figure(figsize=plt.figaspect(1))
ax = fig.gca(projection='3d')
ax.plot([0, v3[0]], [0, v3[1]], [0, v3[2]], linewidth=3)

# make the plot look nicer
ax.plot([0, 0], [0, 0], [-4, 4], 'k--')
ax.plot([0, 0], [-4, 4], [0, 0], 'k--')
ax.plot([-4, 4], [0, 0], [0, 0], 'k--')
plt.show()

# for addition and subtraction, you don't want to use list data type but instead np.array so u can say v2 + v3, whereas list will concatenate them
# two vectors in R2
v1 = np.array([3, -1])
v2 = np.array([2, 4])

v3 = v1 + v2

# plot them
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='v1')
plt.plot([0, v2[0]] + v1[0], [0, v2[1]] + v1[1], 'r', label='v2')
plt.plot([0, v3[0]], [0, v3[1]], 'k', label='v1+v2')

plt.legend()
plt.axis('square')
plt.axis((-6, 6, -6, 6))
plt.grid()
plt.show()

# vector and scalar multiplication
v1 = np.array([3, -1])

# lambda l is the scalar
l = 2.3
v1m = v1 * l  # scalar-modulated

# plot them
plt.plot([0, v1[0]], [0, v1[1]], 'b', label='$v_1$')
plt.plot([0, v1m[0]], [0, v1m[1]], 'r:', label='$\lambda v_1$')

plt.legend()
plt.axis('square')
axlim = max([max(abs(v1)), max(abs(v1m))]) * 1.5  # dynamic axis lim
plt.axis((-axlim, axlim, -axlim, axlim))  # allows the scale of graph to be dynamic based on what lamda is
plt.grid()
plt.show()

## many ways to compute the dot product
v1 = np.array([1, 2, 3, 4, 5, 6])
v2 = np.array([0, -4, 4, -3, 6, 5])

# method 1
dp1 = sum(np.multiply(v1, v2))

# method 2: recommended method
dp2 = np.dot(v1, v2)

# method 3
dp3 = np.matmul(v1, v2)

# method 4
dp4 = 0  # initialize

# loop over elements
for i in range(len(v1)):
    # multiply corresponding element and sum
    dp4 = dp4 + v1[i] * v2[i]

print(dp1, dp2, dp3, dp4)

## Distributive property

# create random vectors
n = 10
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot(a, (b + c))
res2 = np.dot(a, b) + np.dot(a, c)

# compare them
print([res1, res2])

# Associative property

# create random vectors
n = 5
a = np.random.randn(n)
b = np.random.randn(n)
c = np.random.randn(n)

# the two results
res1 = np.dot(a, np.dot(b, c))
res2 = np.dot(np.dot(a, b), c)

# compare them
print(res1)
print(res2)
print(
    "as u can see, they are not equal.. dot product is not associative bc it produces scalar vector multiplication on "
    "2nd product")

# special cases where associative property works!
# 1) one vector is the zeros vector
# 2) a==b==c


# vector length
# pythagorean theorem- the length of the vector is the squareroot of the sum of the squared elements

v1 = [1, 2, 3, 4, 5, 6]
v1l = np.sqrt(sum(np.multiply(v1, v1)))
# or take the norm directly
v1lnorm = np.linalg.norm(v1)
print(v1l, v1lnorm)


