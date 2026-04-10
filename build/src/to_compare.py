from scipy.integrate import solve_ivp

def get_sol(t, y0, f):
    y = solve_ivp(f, t_span=[t[0], t[-1]], y0=[y0], t_eval=t, method="RK45")
    y = y.y[0]
    return y