import numpy as np
import matplotlib.pyplot as plt


#system
#y'' + ay' + by = 0
a = 0.5
b = 2
y_0 = 0
dy_0 = 1
h = 1e-2
t = np.linspace(0, 10, int(10/1e-2))

def solve(_y_0, _dy_0, _a, _b, _t, _h):
    u = [_dy_0]
    v = [_y_0]
    n = len(_t)
    for i in range(n-1):
        v_next = v[-1]+_h*u[-1]
        u_next = (1-_h*_a)*u[-1]-_h*_b*v[-1]
        v.append(v_next)
        u.append(u_next)
    return v
y = solve(y_0, dy_0, a, b, t, h)

plt.plot(t, y)
plt.show()