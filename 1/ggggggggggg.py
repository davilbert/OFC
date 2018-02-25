import numpy as np
import matplotlib
from matplotlib import pylab,mlab,pyplot,cm
plt = pyplot
from mpl_toolkits.mplot3d import Axes3D

IMAGE = plt.figure()
ax = IMAGE.add_subplot(111, projection='3d')
def ColorOfSpiral(START, FINISH, color):
    z = np.linspace(-16, 16, 1000)
    g='white'
    theta = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
    r = 1
    x = - r * np.sin(theta)
    y = - r * np.cos(theta)
    if ((not z.all() > START) and (not z.all() < FINISH)):
        z1 = np.linspace(START, FINISH, 1000)
        ax.scatter(x,y,z1,c=color,s=1)
    elif(z.any()<=START):
        z2 = np.linspace(-16, START, 1000)
        ax.scatter(x,y,z2,c=g,s=1)
    elif (z.any()>=FINISH):
        z3 = np.linspace(FINISH, 16, 1000)
        ax.scatter(x,y,z3,c=g,s=1)

ColorOfSpiral(1, 5, 'blue')
plt.show()
