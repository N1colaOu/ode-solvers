import src.euler_frw as efr
import src.euler_bwd as ebw
import src.heun as rk2
import src.rk4 as rk4
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return -1000*(y-np.cos(t))
t_start = 0.0
t_end = 10.0
y0 = 1.0

err_eulerf = []
err_eulerb= []
err_heun = []
err_rk4 = []
N = []
h = []
t = np.linspace(t_start, t_end, int(1e8))
solution = 1000*(np.sin(t) + 1000*np.cos(t))/(1000**2+1) + 1/(np.exp(1000*t)*(1000**2+1))
for i in range(3, 14):
    N.append(2**i)
    t = np.linspace(t_start, t_end, N[-1])
    h.append(t[1]-t[0])
    eulerf_y = efr.get_sol(t, y0, f)
    eulerb_y = ebw.get_sol(t, y0, f)
    heun_rk2_y = rk2.get_sol(t, y0, f)
    rk4_y = rk4.get_sol(t, y0, f)

    err_eulerf.append(np.abs(solution[-1]-eulerf_y[-1]))
    err_eulerb.append(np.abs(solution[-1]-eulerb_y[-1]))
    err_heun.append(np.abs(solution[-1]-heun_rk2_y[-1]))
    err_rk4.append(np.abs(solution[-1]-rk4_y[-1]))

log_eulerf_y = np.log10(err_eulerf)
log_eulerb_y = np.log10(err_eulerb)
log_heun_y = np.log10(err_heun)
log_rk4_y = np.log10(err_rk4)
log_h_x = np.log10(h)

conv_eulerf = np.log10(err_eulerf[-2]/err_eulerf[-1])/np.log10(h[-2]/h[-1])
conv_eulerb = np.log10(err_eulerb[-2]/err_eulerb[-1])/np.log10(h[-2]/h[-1])
conv_heun = np.log10(err_heun[-2]/err_heun[-1])/np.log10(h[-2]/h[-1])
conv_rk4 = np.log10(err_rk4[-2]/err_rk4[-1])/np.log10(h[-2]/h[-1])

print("Convergence rate of Forward Euler: ", conv_eulerf, ", Theoretical value: 1")
print("Convergence rate of Backward Euler: ", conv_eulerb, ", Theoretical value: 1")
print("Convergence rate of Heun: ", conv_heun, ", Theoretical value: 2")
print("Convergence rate of RK4: ", conv_rk4, ", Theoretical value: 4")

line1f = log_h_x + log_eulerf_y[-1] - log_h_x[-1]
line1b = log_h_x + log_eulerb_y[-1] - log_h_x[-1]
line2 = 2*log_h_x + log_heun_y[-1] - log_h_x[-1]*2
line4 = 4*log_h_x + log_rk4_y[-1] - log_h_x[-1]*4

plt.figure()
#euler forward
plt.subplot(221)
plt.plot(log_h_x, log_eulerf_y)
plt.plot(log_h_x, line1f)
plt.scatter(log_h_x, log_eulerf_y)
plt.title("Forward Euler")
plt.legend(["Actual Error", "Theoretical Error"], loc = 'upper left')
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#euler back2ward
plt.subplot(222)
plt.plot(log_h_x, log_eulerb_y)
plt.plot(log_h_x, line1b)
plt.scatter(log_h_x, log_eulerb_y)
plt.title("Backward Euler")
plt.legend(["Actual Error", "Theoretical Error"], loc = 'upper left')
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#adaptive
plt.subplot(223)
plt.plot(log_h_x, log_heun_y)
plt.plot(log_h_x, line2)
plt.scatter(log_h_x, log_heun_y)
plt.title("Heun/RK2")
plt.legend(["Actual Error", "Theoretical Error"], loc = 'upper left')
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#heun
plt.subplot(224)
plt.plot(log_h_x, log_rk4_y)
plt.plot(log_h_x, line4)
plt.scatter(log_h_x, log_rk4_y)
plt.title("RK4")
plt.legend(["Actual Error", "Theoretical Error"], loc = 'upper left')
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")

plt.subplots_adjust(top=0.87, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
plt.suptitle("Error Comparison")
plt.savefig('err_stiff.png')
plt.show()

