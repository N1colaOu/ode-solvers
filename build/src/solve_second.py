def solve(_y_0, _dy_0, _a, _b, _t):
    h = _t[1] - _t[0]
    u = [_dy_0]
    v = [_y_0]
    n = len(_t)
    for i in range(n-1): # solves system of two ODE
        v_next = v[-1]+h*u[-1]
        u_next = (1-h*_a)*u[-1]-h*_b*v[-1]
        v.append(v_next)
        u.append(u_next)
    return v