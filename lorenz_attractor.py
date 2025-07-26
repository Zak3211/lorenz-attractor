import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

plt.ion()
plt.rcParams['toolbar'] = 'None'

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

ax.set_xlim(-30, 30) 
ax.set_ylim(-70, 70)  
ax.set_zlim(-30, 70) 

ax.set_facecolor('black')
fig.patch.set_facecolor('black')
ax.grid(False)
ax.set_axis_off()

fig.canvas.manager.set_window_title("Lorenz Attractor")

ax.xaxis.pane.set_facecolor('black')
ax.yaxis.pane.set_facecolor('black')
ax.zaxis.pane.set_facecolor('black')


def lorenz(xyz, *, s=  10, r = 28,  b = 2.5):
    x = xyz[0]
    y = xyz[1]
    z = xyz[2]
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return [x_dot, y_dot, z_dot]

num_steps = 10000
dt = 0.01

x, y, z = [0],[1],[1.5]

line, = ax.plot(x, y, z, color = 'white')

for i in range(num_steps):
    temp = lorenz([x[i], y[i], z[i]])

    x.append(x[i] +temp[0]*dt)
    y.append(y[i] +temp[1]*dt)
    z.append(z[i] +temp[2]*dt)
    
    line.set_data(x, y)
    line.set_3d_properties(z)
    plt.draw()
    plt.pause(0.001)

plt.ioff()
plt.show()
