import numpy as np
import matplotlib.pyplot as plt


v1 = np.array([-.3, .6])

mu = 1/np.linalg.norm(v1)

v1n = v1*mu

# plot them
plt.plot([0, v1n[0]],[0, v1n[1]],'r',label='v1-norm',linewidth=5)
plt.plot([0, v1[0]],[0, v1[1]],'b',label='v1')

# axis square
plt.axis('square')
plt.axis(( -6, 6, -6, 6 ))
plt.grid()
plt.legend()
plt.show()