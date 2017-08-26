import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d

#The following code serves to set the axes color (and not the background) to `axes.facecolor`
#This is a known issue of matplotlib's 3D plots ( https://stackoverflow.com/questions/11448972/changing-the-background-color-of-the-axes-planes-of-a-matplotlib-3d-plot )
from matplotlib import rcParams
import matplotlib.colors as colors
facecolor = colors.hex2color(rcParams['axes.facecolor'])
rcParams['axes.facecolor'] = 'FFFFFF'

fig = plt.figure()
ax = fig.gca(projection='3d')
X, Y, Z = axes3d.get_test_data(0.05)
ax.plot_surface(X, Y, Z, rstride=8, cstride=8, alpha=0.3)
cset = ax.contourf(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
cset = ax.contourf(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)

ax.w_xaxis.set_pane_color(facecolor)
ax.w_yaxis.set_pane_color(facecolor)
ax.w_zaxis.set_pane_color(facecolor)

ax.set_xlabel('X')
ax.set_xlim(-40, 40)
ax.set_ylabel('Y')
ax.set_ylim(-40, 40)
ax.set_zlabel('Z')
ax.set_zlim(-100, 100)
