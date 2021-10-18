import numpy as np
import matplotlib.pyplot as plt

# set S
S1 = np.array([1, 1, 0])
S2 = np.array([1, 7, 0])

# vectors v and w
v = np.array([1, 2, 0])
w = np.array([3, 2, 1])

# draw vectors
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot([0, S1[0]],[0, S1[1]],[.1, S1[2]+.1],'r',linewidth=3)
ax.plot([0, S2[0]],[0, S2[1]],[.1, S2[2]+.1],'r',linewidth=3)

ax.plot([0, v[0]],[0, v[1]],[.1, v[2]+.1],'g',linewidth=3)
ax.plot([0, w[0]],[0, w[1]],[0, w[2]],'b')

# now draw plane
xx, yy = np.meshgrid(range(-15,16), range(-15,16))
cp = np.cross(S1,S2)
z1 = (-cp[0]*xx - cp[1]*yy)*1./cp[2]
ax.plot_surface(xx,yy,z1)

plt.show()
