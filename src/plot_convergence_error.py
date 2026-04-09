import euler_frw as efr
import euler_bwd as ebw
import heun as rk2
import rk4 as rk4
import to_compare as cmp
import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return 2*t * np.exp(-t**2)
t_start = 0.0
t_end = 10.0
y0 = 1.0



err_eulerf = []
err_eulerb= []
err_heun = []
err_rk4 = []
h = []
for i in range(3, 10):
    h.append(2**(-i))

    eulerf_y = efr.get_sol(t_start, t_end, h[-1], y0, f)
    eulerb_y = ebw.get_sol(t_start, t_end, h[-1], y0, f)
    heun_rk2_y = rk2.get_sol(t_start, t_end, h[-1], y0, f)
    rk4_y = rk4.get_sol(t_start, t_end, h[-1], y0, f)
    solution = cmp.get_sol(t_start, t_end, h[-1], y0, f)

    err_eulerf.append(np.abs(solution[-1]-eulerf_y[-1]))
    err_eulerb.append(np.abs(solution[-1]-eulerb_y[-1]))
    err_heun.append(np.abs(solution[-1]-heun_rk2_y[-1]))
    err_rk4.append(np.abs(solution[-1]-rk4_y[-1]))

log_eulerf_y = np.log10(err_eulerf)
log_eulerb_y = np.log10(err_eulerb)
log_heun_y = np.log10(err_heun)
log_rk4_y = np.log10(err_rk4)
log_h_x = np.log10(h)

conv_eulerf = []
conv_eulerb = []
conv_heun = []
conv_rk4 = []
for i in range(0, 6):
    conv_eulerf.append(np.log10(err_eulerf[i]/err_eulerf[i+1])/np.log10(h[i]/h[i+1]))
    conv_eulerb.append(np.log10(err_eulerb[i]/err_eulerb[i+1])/np.log10(h[i]/h[i+1]))
    conv_heun.append(np.log10(err_heun[i]/err_heun[i+1])/np.log10(h[i]/h[i+1]))
    conv_rk4.append(np.log10(err_rk4[i]/err_rk4[i+1])/np.log10(h[i]/h[i+1]))
print("Convergence rate of Forward Euler: ", conv_eulerf[0], ", Theoretical value: 1")
print("Convergence rate of Backward Euler: ", conv_eulerb[0], ", Theoretical value: 1")
print("Convergence rate of Heun: ", conv_heun[0], ", Theoretical value: 2")
print("Convergence rate of RK4: ", conv_rk4[0], ", Theoretical value: 4")

x = np.linspace(np.log10(h[0]), np.log10(h[-1]))
line1 = x
line2 = 2*x
line4 = 4*x

plt.figure()
#euler forward
plt.subplot(221)
plt.plot(log_h_x, log_eulerf_y)
plt.plot(x, line1)
plt.title("Forward Euler")
plt.legend(["Slope of Actual Error", "Slope of Theoretical Error"])
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#plt.plot([[-3,-3], [2,2]])
#plt.xlim([t_start, t_end])
#euler back2ward
plt.subplot(222)
plt.plot(log_h_x, log_eulerb_y)
plt.plot(x, line1)
plt.title("Backward Euler")
plt.legend(["Slope of Actual Error", "Slope of Theoretical Error"])
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#plt.xlim([t_start, t_end])
#adaptive
plt.subplot(223)
plt.plot(log_h_x, log_heun_y)
plt.plot(x, line2)
plt.title("Heun/RK2")
plt.legend(["Slope of Actual Error", "Slope of Theoretical Error"])
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#plt.xlim([t_start, t_end])
#heun
plt.subplot(224)
plt.plot(log_h_x, log_rk4_y)
plt.plot(x, line4)
plt.title("RK4")
plt.legend(["Slope of Actual Error", "Slope of Theoretical Error"])
plt.xlabel("log10(h)")
plt.ylabel("log10(E(h))")
#plt.xlim([t_start, t_end])

plt.subplots_adjust(top=0.87, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
plt.suptitle("Error Comparison")
plt.show()


