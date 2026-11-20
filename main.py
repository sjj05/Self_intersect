import numpy as np
from self_intersect import *
from param_eqns import *

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
