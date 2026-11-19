import numpy as np
import matplotlib.pyplot as plt

def findPeriod(fxy, dt):
    t = 0.
    x0, y0 = fxy(t)
    
    x = 1e99 # TAKE CARE:   in theory starting value could be this big,
    y = 1e99 #              (in practice probably not)

    while not (np.isclose(x,x0, atol = 1e-5) and np.isclose(y,y0, atol = 1e-5)):
        t+=dt
        x,y = fxy(t)
    
    return t

def toCartesian(fxy,tt):
    # Takes tt a numpy array
    xx, yy = fxy(tt)

    return(xx,yy)

def plotParametric(fxy,tt):
    xx,yy = toCartesian(fxy,tt)

    plt.plot(xx,yy,"-")

    plt.grid(alpha = 0.5)
    plt.axis("square")

    plt.xlabel("x")
    plt.ylabel("y")

def selfIntersect(fxy, tt):
    xx, yy = toCartesian(fxy, tt)

    points = np.column_stack((xx, yy))
    intersections = []

    def cross(a, b):
        return a[0]*b[1] - a[1]*b[0]

    for i in range(len(points) - 1):
        p = points[i]
        r = points[i+1] - p

        for j in range(i + 2, len(points) - 1):

            # Skip first and last segments if curve is closed
            if i == 0 and j == len(points) - 2:
                continue

            q = points[j]
            s = points[j+1] - q

            denominator = cross(r, s)

            if np.isclose(denominator, 0, atol=1e-12):
                continue

            u = cross(q-p, s) / denominator
            v = cross(q-p, r) / denominator

            if 0 <= u <= 1 and 0 <= v <= 1:
                intersection = p + u*r

                if not any(
                    np.allclose(intersection, pt, atol=1e-4)
                    for pt in intersections
                ):
                    intersections.append(intersection)

    return np.array(intersections).reshape(-1, 2)
