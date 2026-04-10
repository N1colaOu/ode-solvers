import src.euler_frw as efr
import src.euler_bwd as ebw
import src.heun as rk2
import src.rk4 as rk4
import src.naive_adapt as adp
import src.to_compare as cmp
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -1000*(y-np.cos(t))
n = 1e2
t_start = 0.0
t_end = 10.0
y0 = 1
t = np.linspace(t_start, t_end, int(n))


euler_f_y = efr.get_sol(t, y0, f)
euler_b_y = ebw.get_sol(t, y0, f)
heun_rk2_y = rk2.get_sol(t, y0, f)
rk4_y = rk4.get_sol(t, y0, f)
adaptive = adp.get_sol(t_start, t_end, t[1]-t[0], y0, f, low=5e-6, high=5e-5)
adaptive_y = adaptive[0]
adaptive_t = adaptive[1]
#solution = cmp.get_sol(t, y0, f)
solution = 1000*(np.sin(t) + 1000*np.cos(t))/(1000**2+1) + 1/(np.exp(1000*t)*(1000**2+1))

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
plt.scatter(adaptive_t, adaptive_y, linewidths=0.017, marker=".", c='r')
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

plt.subplots_adjust(top=0.87, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
plt.suptitle("Solution Comparison")
plt.show()


