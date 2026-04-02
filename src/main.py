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
h = 5e-2
t_start = 0.0
t_end = 10.0
y0 = 0.0


euler_f_y = efr.get_sol(t_start, t_end, h, y0, f)
euler_b_y = ebw.get_sol(t_start, t_end, h, y0, f)
heun_rk2_y = rk2.get_sol(t_start, t_end, h, y0, f)
rk4_y = rk4.get_sol(t_start, t_end, h, y0, f)
adaptive = adp.get_sol(t_start, t_end, h, y0, f)
adaptive_y = adaptive[0]
adaptive_t = adaptive[1]
solution = cmp.get_sol(t_start, t_end, h, y0, f)
t = np.linspace(t_start, t_end, int((t_end-t_start)/h))


plt.figure()
#euler forward
plt.subplot(321)
plt.plot(t, euler_f_y)
#plt.scatter(t, euler_f_y, linewidths=1e-1, marker="x")
plt.title("Forward Euler")
plt.xlim([t_start, t_end])
#euler back2ward
plt.subplot(322)
plt.plot(t, euler_b_y)
plt.title("Backward Euler")
plt.xlim([t_start, t_end])
#adaptive
plt.subplot(323)
plt.plot(adaptive_t, adaptive_y)
plt.scatter(adaptive_t, adaptive_y, linewidths=0.06, marker="+", c='r')
plt.title("Adaptive Method")
plt.xlim([t_start, t_end])
#heun
plt.subplot(324)
plt.plot(t, heun_rk2_y)
plt.title("Heun/RK2")
plt.xlim([t_start, t_end])
#rk4
plt.subplot(325)
plt.plot(t, rk4_y)
plt.title("RK4")
plt.xlim([t_start, t_end])
#solution to compare with
plt.subplot(326)
plt.plot(t, solution)
plt.title("Most Accurate Version")
plt.xlim([t_start, t_end])

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
plt.show()


