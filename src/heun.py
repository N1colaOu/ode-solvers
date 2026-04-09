def get_sol(t, y0, f):
    h = t[1] - t[0]
    def y_n1(t_n, y_n, h):
        A = f(t_n, y_n)
        B = f(t_n + h,  y_n + A*h)
        return y_n + (A + B) * h / 2

    y = [y0]
    for i in range(len(t)-1):
        y.append(y_n1(t[i], y[i], h))
    return y