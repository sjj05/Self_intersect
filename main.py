import numpy as np
from self_intersect import *

def fx(t):
    return 8 * np.cos(20 * t)

def fy(t):
    return 12 * np.sin(10 * t - np.pi/3)

def fxy(t):
    return fx(t), fy(t)

def fx2(t):
    return np.sin(3*t)

def fy2(t):
    return np.sin(4*t)

def fxy2(t):
    return fx2(t), fy2(t)

period = findPeriod(fxy,1e-5)

tt = np.linspace(0,2*np.pi,500)

plotParametric(fxy2,tt)

xx,yy = toCartesian(fxy2, tt)
plt.plot(xx[0], yy[0], "o", markersize = 5, label = "t=0")

intersections = selfIntersect(fxy2, tt)

for i, (x, y) in enumerate(intersections):
    plt.plot(x, y, 'ro', markersize=5,
             label="Self-intersection" if i == 0 else None)

plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()

plt.show()
