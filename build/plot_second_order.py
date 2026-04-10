import numpy as np
import matplotlib.pyplot as plt
import src.solve_second as osc

#y'' + ay' + by = 0
#Input paramters:
y_0 = 0
dy_0 = 1
a = 0.5
b = 2
n = 1e2
t_start = 0
t_end = 10


t = np.linspace(t_start, t_end, int(n))
y = osc.solve(y_0, dy_0, a, b, t)
plt.plot(t, y)
plt.title("Second Order")
plt.xlim([t_start, t_end])
plt.xlabel("t")
plt.ylabel("y(t)")
plt.savefig("second_ord.png")
plt.show()