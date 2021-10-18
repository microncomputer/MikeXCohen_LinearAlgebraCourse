import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v1 = [16,-2,4]
v2 = [.5, 2, -1]

#compute the angle between the two vectors
theta = np.arccos(np.dot(v1, v2)/(np.linalg.norm(v1) * np.linalg.norm(v2)))
print(np.dot(v1,v2))
print(theta)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0,v1[0]], [0, v1[1]], [0, v1[2]], 'b')
ax.plot([0,v2[0]], [0, v2[1]], [0, v2[2]], 'r')

plt.axis((-6,6,-6,6))
plt.title('angle between vectors: %s radians' %theta)
plt.show()
