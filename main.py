import numpy as np
from self_intersect import *

def fx(t):
    return 8 * np.cos(20 * t)

def fy(t):
    return 12 * np.sin(10 * t - np.pi/3)

def fxy(t):
    return fx(t), fy(t)

def ljousx(t):
    return np.sin(3*t)

def ljousy(t):
    return np.sin(4*t)

def ljous(t):
    return ljousx(t), ljousy(t)

def hypox(t):
    R = 32
    r = 14
    d = 6

    return (R-r)*np.cos(t) + d*np.cos(((R-r)/r)*t)

def hypoy(t):
    R = 32
    r = 14
    d = 6

    return (R-r)*np.sin(t) - d*np.sin(((R-r)/r)*t)

def hypo(t):
    return hypox(t), hypoy(t)

period = 2 * np.pi * 14 / np.gcd(32,14)

tt = np.linspace(0,period,500)

plotParametric(hypo,tt)

xx,yy = toCartesian(hypo, tt)
plt.plot(xx[0], yy[0], "o", markersize = 5, label = "t=0")

intersections = selfIntersect(hypo, tt)

for i, (x, y) in enumerate(intersections):
    plt.plot(x, y, 'ro', markersize=5,
             label="Self-intersection" if i == 0 else None)

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

plt.show()
