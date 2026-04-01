import numpy as np
import matplotlib.pyplot as plt

#------------------------------------#
"""
#input your function here
def f(t, y):
    return y - 0.5*np.exp(t/2)*np.sin(5*t) + 5*np.exp(t/2)*np.cos(5*t)
h = 1e-2
t_start = 0.0
t_end = 10.0
y0 = 0.0
#------------------------------------#
"""

def get_sol(t_start, t_end, h, y0, f):
    def y_n1(t_n, y_n, h):
        A = f(t_n, y_n)
        B = f(t_n + h,  y_n + A*h)
        return y_n + (A + B) * h / 2

    t_span = np.abs(t_end - t_start)
    n = int(t_span/h)
    t = np.linspace(t_start, t_end, n)
    y = np.zeros(n, dtype=float)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y_n1(t[i], y[i], h)

    return y