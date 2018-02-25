import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cmx
#a = int (input())
mpl.rcParams['legend.fontsize'] = 100000

#theta = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
#z = np.linspace(-6, 6, 1000)
#r = 5.0
#x = r * np.sin(theta)
#y = r * np.cos(theta)
cs = 0.2

#theta1 = np.linspace(10 * np.pi, -10 * np.pi, 1000)
#z11 = np.linspace(5, -5, 1000)
#r11 = 5.0
#x1 = -r1 * np.sin(theta1)
#y1 =- r1 * np.cos(theta1)
cs1 = 0.2


colorsMap='jet'
cm = plt.get_cmap(colorsMap)
cNorm = mpl.colors.Normalize(vmin=min(cs), vmax=max(cs))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cm)
cm1 = plt.get_cmap(colorsMap)
cNorm1 = mpl.colors.Normalize(vmin=min(cs1), vmax=max(cs1))
scalarMap = cmx.ScalarMappable(norm=cNorm1, cmap=cm1)
fig = plt.figure()
scalarMap.set_array(cs)
fig1 = plt.figure()
scalarMap.set_array(cs1)


ax = fig.add_subplot(111, projection='3d')
k = -5.0
for i in np.arange(-15.0,k, 1.0):
    theta1 = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
    z2 = np.linspace(-i, i, 1000)
    r2 = z2**2 + 1
    x2 = -r2 * np.sin(theta1)
    y2 =- r2 * np.cos(theta1)
    #ax.scatter(x2, y2, z2, c='green', marker='_', s=1, lw=1.0) # lw=2.5
t = 5
for i in np.arange(-5.0,t, 1.0):
    theta1 = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
    z1 = np.linspace(-i, i, 1000)
    r1 = 1 #z1**2 + 1
    x1 = -r1 * np.sin(theta1)
    y1 =- r1 * np.cos(theta1)
    ax.scatter(x1, y1, z1, c='red', marker='_', s=1, lw=1.0) # lw=2.5
#plt.colorbar(scalarMap)
p = 15
for i in np.arange(5.0,p, 1.0):
    theta3 = np.linspace(-10 * np.pi, 10 * np.pi, 1000)
    z3 = np.linspace(-i, i, 1000)
    r3 = z3**2 + 1
    x3 = -r3 * np.sin(theta3)
    y3 =- r3 * np.cos(theta3)
    #ax.scatter(x3, y3, z3, c='black', marker='_', s=1,lw=1.0) # lw=2.5
plt.show()
#ax.scatter(x, y, z, c='red', marker='_', s=1)
#plt.colorbar(scalarMap)
#ax1 = fig1.add_subplot(111, projection='3d')
#ax.scatter(x1,y1,z1, c='red', marker='_', s=1)


