from os import path
almost_this_path = path.abspath(path.dirname(__file__))
this_path_base, _ = path.split(almost_this_path)
data_path = path.join(this_path_base,"data")

import numpy as np
import matplotlib.pyplot as plt


# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = np.loadtxt(path.join(data_path,"radii.csv"))
widths = np.loadtxt(path.join(data_path,"widths.csv"))

ax = plt.subplot(1,1,1, projection='polar')
bars = ax.bar(theta, radii, width=widths, bottom=0.0)

# Use custom colors and opacity
for rad, bar in zip(radii, bars):
    a = []
    for i in theta:
        a_i = i*rad
        a.append(a_i)
    bar.set_facecolor(plt.cm.viridis(rad / 10.))
    bar.set_alpha(0.5)
