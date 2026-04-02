import numpy as np

def get_sol(t_start, t_end, h, y0, f):
    def adjust_h(t_n, y_n, h, tol1 = 1e-4, tol2 = 2e-4):
        A = f(t_n, y_n)
        yE = y_n + h*A
        B = f(t_n + h,  y_n + A*h)
        yH = y_n + (A + B) * h / 2
        delta = np.abs(yE-yH)
        if delta > tol1:
            h = h/2
        elif delta < tol2:
            h = h*2
        return h
    def y_n1(tn, yn, h):
        adjust_h(tn, yn, h)
        return yn + h*f(tn, yn)

    t_span = np.abs(t_end - t_start)
    n = int(t_span/h)
    t = np.linspace(t_start, t_end, n)
    y = np.zeros(n, dtype=float)
    y[0] = y0
    for i in range(0, n-1):
        y[i+1] = y_n1(t[i], y[i], h)

    return y