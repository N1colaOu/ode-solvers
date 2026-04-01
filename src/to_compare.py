import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def get_sol(t_start, t_end, h, y0, f):
    n = int((t_end - t_start) / h)
    t = np.linspace(t_start, t_end, n)
    y = solve_ivp(f, (t_start, t_end), [y0], t_eval=t)
    y = y.y[0]
    return y, t