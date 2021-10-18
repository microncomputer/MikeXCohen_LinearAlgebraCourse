import numpy as np
import matplotlib.pyplot as plt

#numpy complex number
z = np.complex(3,4)
print(np.linalg.norm(z))

#by transpose
print(np.transpose(z)*z)

#by hermitian transpose
print(np.transpose(z.conjugate()) * z)

