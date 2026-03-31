import numpy as np
import matplotlib.pyplot as plt

#------------------------------------%  
def f(t, y):
    #input your function here
    return y - 0.5*np.exp(t/2)*np.sin(5*t) + 5*np.exp(t/2)*np.cos(5*t)
h = 0.05
t_start = 0
t_end = 10
y0 = 0
#------------------------------------%

def y_n1(t_n, y_n, h):
    A = f(t_n, y_n)
    B = f(t_n + h,  y_n + A*h)
    return y_n + (A + B) * h / 2

t_span = float(np.abs(t_end - t_start))
n = int(t_span/h)
t = np.linspace(t_start, t_end, n)
y = np.zeros(n, dtype=float)
y[0] = y0
for i in range(0, n-1):
    y[i+1] = y_n1(t[i], y[i], h)


fig1, ax1 = plt.subplots(figsize = (6, 5), layout = 'constrained')
ax1.plot(t, y)

ax1.set_xlabel('t')
ax1.set_ylabel('y(t)')
ax1.legend(['RK2'])
ax1.set_title('RK2')
plt.show()

#plt.plot(t, y)

#plt.xlabel('t')
#plt.ylabel('y(t)')
#plt.legend(['RK2'])
#plt.title('RK2')


