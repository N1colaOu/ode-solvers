import numpy as np
from scipy.integrate import solve_ivp

def get_sol(t_start, t_end, h, y0, f):
    n = int((t_end - t_start) / h)
    t = np.linspace(t_start, t_end, n)
    y = solve_ivp(f, t_span=[t[0], t[-1]], y0=[y0], t_eval=t, method="RK45")
    y = y.y[0]
    return y