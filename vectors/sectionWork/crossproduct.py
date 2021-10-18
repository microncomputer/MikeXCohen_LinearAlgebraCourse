import numpy as np
import matplotlib.pyplot as plt

v1 = [-3, 2, 5]
v2 = [4, -3, 0]

c1 = np.cross(v1, v2)
print(c1)

# manual method
c2 = [[v1[1] * v2[2] - v1[2] * v2[1]], [v1[2] * v2[0] - v1[0] * v2[2]], [v1[0] * v2[1] - v1[1] * v2[0]]]
print(c2)

fig = plt.figure()
ax = fig.gca(projection='3d')

# draw plane defined by span of v1 and v2
xx, yy = np.meshgrid(np.linspace(-10,10,10),np.linspace(-10,10,10))
z1 = (-c1[0]*xx - c1[1]*yy)/c1[2]
ax.plot_surface(xx,yy,z1,alpha=.2)

## plot the two vectors
ax.plot([0, v1[0]],[0, v1[1]],[0, v1[2]],'k')
ax.plot([0, v2[0]],[0, v2[1]],[0, v2[2]],'k')
ax.plot([0, c1[0]],[0, c1[1]],[0, c1[2]],'r')


ax.view_init(azim=150,elev=45)
plt.show()