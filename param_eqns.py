import numpy as np

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
