import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Spiral parameters
#samNum = 1000
#spConst = 5.0
#t = np.linspace(0,89*np.pi, samNum)

#T, Z = np.meshgrid(t, [0,1])
#X = spConst * (np.cos(T) + T* np.sin(T))
#Y = spConst * (np.sin(T) - T * np.cos(T))

# Coordinates of involute spiral on xy-plane
#coords = np.zeros([samNum, 3])
#coords[:,0] = spConst * (np.cos(t) + t * np.sin(t)) # x coord
#coords[:,1] = spConst * (np.sin(t) - t * np.cos(t)) # y coord

# Paramters for 2D Gaussian surface
#amp = 200
#sigma_x = 75.0
#sigma_y = 75.0
#theta = np.pi
#a = np.cos(theta)**2 / (2 * sigma_x**2) + np.sin(theta)**2 / (2 * sigma_y**2)
#b = -np.sin(2 * theta) / (4 * sigma_x**2) + np.sin(2 * theta) / (4 * sigma_y**2)
#c = np.sin(theta)**2 / (2 * sigma_x**2) + np.cos(theta)**2 / (2 * sigma_y**2)

# z coords of spiral projected onto Gaussian surface
#coords[:,2] = amp * np.exp(-(a * coords[:,0]**2 - 2 * b * coords[:,0]*coords[:,1] + c * coords[:,1]**2)) # z coord

#Z[1,:] = coords[:,2]
#ax.plot_surface(X,Y,Z)

# plot 3D spiral
#ax.scatter(coords[:,0], coords[:,1], coords[:,2], s=1, c='k')

#ax.set_xlabel('X axis')
#ax.set_ylabel('Y axis')
#ax.set_zlabel('Z axis')

###second spiral

fig_1 = plt.figure()
ax = fig_1.add_subplot(111, projection='3d')

# Spiral parameters
samNum1 = 1000
spConst1 = 5.0
t = np.linspace(0,89*np.pi, samNum1)

T, Z = np.meshgrid(t, [0,1])
X = spConst1 * (np.cos(T) + T* np.sin(T))
Y = spConst1 * (np.sin(T) - T * np.cos(T))

# Coordinates of involute spiral on xy-plane
coords = np.zeros([samNum1, 3])
coords[:,0] = spConst1 * (np.cos(t) + t * np.sin(t)) # x coord
coords[:,1] = spConst1 * (np.sin(t) - t * np.cos(t)) # y coord

# Paramters for 2D Gaussian surface
amp1 = 200
sigma_x1 = -75.0
sigma_y1 = -75.0
theta1 = np.pi
a1 = np.cos(theta1)**2 / (2 * sigma_x1**2) + np.sin(theta1)**2 / (2 * sigma_y1**2)
b1 = np.sin(2 * theta1) / (4 * sigma_x1**2) - np.sin(2 * theta1) / (4 * sigma_y1**2)
c1 = -np.sin(theta1)**2 / (2 * sigma_x1**2) + np.cos(theta1)**2 / (2 * sigma_y1**2)

# z coords of spiral projected onto Gaussian surface
coords[:,2] = amp1 * np.exp(-(a1 * coords[:,0]**2 - 2 * b1 * coords[:,0]*coords[:,1] + c1 * coords[:,1]**2)) # z coord

Z[1,:] = coords[:,2]
ax.plot_surface(X,Y,Z)

# plot 3D spiral
ax.scatter(coords[:,0], coords[:,0], coords[:,2], s=1, c='k')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

###third spiral

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Spiral parameters
samNum = 1000
spConst = -5.0
t = np.linspace(0,89*np.pi, samNum)

T, Z = np.meshgrid(t, [0,1])
X = spConst * (np.cos(T) + T* np.sin(T))
Y = spConst * (np.sin(T) - T * np.cos(T))

# Coordinates of involute spiral on xy-plane
coords = np.zeros([samNum, 3])
coords[:,0] = spConst * (np.cos(t) + t * np.sin(t)) # x coord
coords[:,1] = spConst * (np.sin(t) - t * np.cos(t)) # y coord

# Paramters for 2D Gaussian surface
amp = 200
sigma_x = -75.0
sigma_y = -75.0
theta = np.pi
a = np.cos(theta)**2 / (2 * sigma_x**2) + np.sin(theta)**2 / (2 * sigma_y**2)
b = np.sin(2 * theta) / (4 * sigma_x**2) - np.sin(2 * theta) / (4 * sigma_y**2)
c = -np.sin(theta)**2 / (2 * sigma_x**2) + np.cos(theta)**2 / (2 * sigma_y**2)

# z coords of spiral projected onto Gaussian surface
coords[:,2] = amp * np.exp(-(a * coords[:,0]**2 - 2 * b * coords[:,0]*coords[:,1] + c * coords[:,1]**2)) # z coord

Z[1,:]= coords[:,2]
ax.plot_surface(X,Y,Z)

# plot 3D spiral
ax.scatter(coords[:,0], coords[:,0], coords[:,2], s=1, c='k')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
plt.show()





















import numpy as np
import matplotlib
from matplotlib import pylab,mlab,pyplot,cm
plt = pyplot
from mpl_toolkits.mplot3d import Axes3D
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
f=int(input())
g=int(input())
h=int(input())

IMAGE = plt.figure()
ax = IMAGE.add_subplot(111, projection='3d')

z = np.linspace(-16, 16, 100)
theta = np.linspace(-10 * np.pi, 10 * np.pi, 100)
r = 1
x = - r * np.sin(theta)
y = - r * np.cos(theta)

if (a==1):
        z1 = np.linspace(-16, -12, 100)
        ax.scatter(x,y,z1,c='red',s=1)
elif (a==2):
        z1 = np.linspace(-16, -12, 100)
        ax.scatter(x,y,z1,c='blue',s=1)
elif (a==3):
        z1 = np.linspace(-16, -12, 100)
        ax.scatter(x,y,z1,c='green',s=1)
elif (a==4):
        z1 = np.linspace(-16, -12, 100)
        ax.scatter(x,y,z1,c='yellow',s=1)
if (b==1):
        z2 = np.linspace(-12, -8, 100)
        ax.scatter(x,y,z2,c='red',s=1)
elif (b==2):
        z2 = np.linspace(-12, -8, 100)
        ax.scatter(x,y,z2,c='blue',s=1)
elif (b==3):
        z2 = np.linspace(-12, -8, 100)
        ax.scatter(x,y,z2,c='green',s=1)
elif (b==4):
        z2 = np.linspace(-12, -8, 100)
        ax.scatter(x,y,z2,c='yellow',s=1)
if (c==1):
        z3 = np.linspace(-8, -4, 100)
        ax.scatter(x,y,z3,c='red',s=1)
elif (c==2):
        z3 = np.linspace(-8, -4, 100)
        ax.scatter(x,y,z3,c='blue',s=1)
elif (c==3):
        z3 = np.linspace(-8, -4, 100)
        ax.scatter(x,y,z3,c='green',s=1)
elif (c==4):
        z3 = np.linspace(-8, -4, 100)
        ax.scatter(x,y,z3,c='yellow',s=1)
if (d==1):
        z4 = np.linspace(-4, 0, 100)
        ax.scatter(x,y,z4,c='red',s=1)
elif (d==2):
        z4 = np.linspace(-4, 0, 100)
        ax.scatter(x,y,z4,c='blue',s=1)
elif (d==3):
        z4 = np.linspace(-4, 0, 100)
        ax.scatter(x,y,z4,c='green',s=1)
elif (d==4):
        z4 = np.linspace(-4, 0, 100)
        ax.scatter(x,y,z4,c='yellow',s=1)
if (e==1):
        z5 = np.linspace(0, 4, 100)
        ax.scatter(x,y,z5,c='red',s=1)
elif (e==2):
        z5 = np.linspace(0, 4, 100)
        ax.scatter(x,y,z5,c='blue',s=1)
elif (e==3):
        z5 = np.linspace(0, 4, 100)
        ax.scatter(x,y,z5,c='green',s=1)
elif (e==4):
        z5 = np.linspace(0, 4, 100)
        ax.scatter(x,y,z5,c='yellow',s=1)
if (f==1):
        z6 = np.linspace(4, 8, 100)
        ax.scatter(x,y,z6,c='red',s=1)
elif (f==2):
        z6 = np.linspace(4, 8, 100)
        ax.scatter(x,y,z6,c='blue',s=1)
elif (f==3):
        z6 = np.linspace(4, 8, 100)
        ax.scatter(x,y,z6,c='green',s=1)
elif (f==4):
        z6 = np.linspace(4, 8, 100)
        ax.scatter(x,y,z6,c='yellow',s=1)
if (g==1):
        z7 = np.linspace(8, 12, 100)
        ax.scatter(x,y,z7,c='red',s=1)
elif (g==2):
        z7 = np.linspace(8, 12, 100)
        ax.scatter(x,y,z7,c='blue',s=1)
elif (g==3):
        z7 = np.linspace(8, 12, 100)
        ax.scatter(x,y,z7,c='green',s=1)
elif (g==4):
        z7 = np.linspace(8, 12, 100)
        ax.scatter(x,y,z7,c='yellow',s=1)
if (h==1):
        z8 = np.linspace(12, 16, 100)
        ax.scatter(x,y,z8,c='red',s=1)
elif (h==2):
        z8 = np.linspace(12, 16, 100)
        ax.scatter(x,y,z8,c='blue',s=1)
elif (h==3):
        z8 = np.linspace(12, 16, 100)
        ax.scatter(x,y,z8,c='green',s=1)
elif (h==4):
        z8 = np.linspace(12, 16, 100)
        ax.scatter(x,y,z8,c='yellow',s=1)

plt.show()
