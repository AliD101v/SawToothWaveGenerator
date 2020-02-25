import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt

"""
References
----------
robjohn (https://math.stackexchange.com/users/13854/robjohn), Equation of a "tilted" sine, URL (version: 2017-09-20): https://math.stackexchange.com/q/2431811
"""
def sawtooth_wave(n, x):
    y = np.zeros_like(x)
    for k in range(1, n + 1):
        y += (comb(2*n, n-k) / comb(2*n, n)) * ( np.sin(k*x) / k )
    return y

points = 1000
periods = 4
lines = 100
# Construct the colormap
cmap = plt.cm.get_cmap('jet')
colors = np.logspace(1, 0, lines)
colors = (colors - colors.min(axis=0)) / (colors.max(axis=0) - colors.min(axis=0))
colors = cmap(colors)
# colors = cmap(1. - colors)
# Create the points
x = np.linspace(0, np.pi * periods, points)

# Create the figure
plt.figure()
for n in range(1, lines + 1):
    y = sawtooth_wave(n, x)
    plt.plot(x, y, c=colors[n-1,:])
plt.show()