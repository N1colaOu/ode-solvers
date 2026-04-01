import euler_frw as efr
import euler_bwd as ebw
import heun as rk2
import rk4 as rk4
import naive_adapt as adp
import to_compare as cmp
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return y - 0.5*np.exp(t/2)*np.sin(5*t) + 5*np.exp(t/2)*np.cos(5*t)
h = 1e-2
t_start = 0.0
t_end = 10.0
y0 = 0.0

euler_f_y = efr.get_sol(t_start, t_end, h, y0, f)[0]
euler_b_y = ebw.get_sol(t_start, t_end, h, y0, f)[0]
heun_rk2_y = rk2.get_sol(t_start, t_end, h, y0, f)[0]
rk4_y = rk4.get_sol(t_start, t_end, h, y0, f)[0]
adaptive_y = adp.get_sol(t_start, t_end, h, y0, f)[0]
#solution = cmp.get_sol(t_start, t_end, h, y0, f)[0]
t = efr.get_sol(t_start, t_end, h, y0, f)[1]


plt.figure()

#euler forward
plt.subplot(321)
plt.plot(t, euler_f_y)
plt.title("Forward Euler")
#euler back2ward
plt.subplot(322)
plt.plot(t, euler_b_y)
plt.title("Backward Euler")
#heun
plt.subplot(323)
plt.plot(t, heun_rk2_y)
plt.title("Heun/RK2")
#rk4
plt.subplot(324)
plt.plot(t, rk4_y)
plt.title("RK4")
#adaptive
plt.subplot(325)
plt.plot(t, adaptive_y)
plt.title("Adaptive Method")
#solution to compare with
#lt.subplot(226)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
plt.show()


