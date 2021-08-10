from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
import pdb
 
fig = plt.figure()
ax = Axes3D(fig)
x=np.arange(-2*np.pi,2*np.pi,0.1)
y=np.arange(-2*np.pi,2*np.pi,0.1)
X, Y = np.meshgrid(x, y)

#Z=np.sin(X)*np.cos(Y)
Z=np.maximum(X,Y)
plt.xlabel('x')
plt.ylabel('y')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()
