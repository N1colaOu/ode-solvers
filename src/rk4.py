import numpy as np

def get_sol(t_start, t_end, h, y0, f):
    def y_n1(t_n, y_n, h):
        A = f(t_n, y_n)
        B = f(t_n + h/2, y_n + A * h / 2)
        C = f(t_n + h/2, y_n+ B * h / 2)
        D = f(t_n + h, y_n + C * h)
        return y_n + (A + 2*B +  2*C + D)* h / 6


    t_span = np.abs(t_end - t_start)
    n = int(t_span/h)
    t = np.linspace(t_start, t_end, n)
    y = np.zeros(n, dtype=float)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y_n1(t[i], y[i], h)

    return y