# ode-solvers
## Mathematics
This project feautures 5 different solvers for ordinary differential equations (ODE's).
- *Forward Euler Method*
- *Backward Euler Method*
- *Heun/RK2 Method*
- *RK4 Method*
- *Primitive Adaptive Method*  
#### Forward Euler Method
The most primitve out of all methods. It is a simple one step evaluation of ODE of type:
$$
y' = f(t, y)
$$
Using the forward finite difference approach for the derivative we get the following algorithm:
$$
y(t_n)' = \frac{y(t_{n+1}) - y(t_n)}{t_{n+1} - t_n} = f(t_n, y(t_n))
$$
$$
y(t_{n+1}) = y(t_n) + hf(t_n, y(t_n))
$$
This gives us the value of the function at the next time step, effectively solving the ODE.
#### Backward Euler Method
Here instead of the forward finite difference, we take the backwards one:
$$
y'(t_n) = \frac{y(t_n) - y(t_{n-1})}{t_n-t_{n-1}}
$$
After plugging into the ODE and displacing the index n one forwards, we get:
$$
y'(t_n) = f(t_n, y(t_n))
$$
$$
y(t_n) = f(t_n, y(t_n))(t_n-t_{n-1}) + y(t_{n-1})
$$
$$
y(t_{n+1}) = f(t_{n+1}, y(t_{n+1}))(t_{n+1}-t_n) + y(t_n)
$$
$$
y_{n+1} = f(t_{n+1}, y_{n+1})(t_{n+1}-t_n) + y_n
$$
Due to the fact, that $y_{n+1}$ is unknown, we cannot evaluate $f(t_{n+1}, y_{n+1})$. If we move everything to the right-hand side of the equation, it becomes a equation with one unknown.
$$
y_{n+1} - f(t_{n+1}, y_{n+1})(t_{n+1}-t_n) - y_n = 0
$$
 Here to find the roots of the equation I have used the Newton-Method to search for a root and afterwards evaluate the rest of the solution.
#### Heun/RK2 Method
More sophisticated method calculating 2 steps each evaluation, correcting and converging faster than Euler Method. For simplicity the step size or size of the little time intervals will be called $h$
$$
    A = f(t_n, y_n)
$$
$$
    B = f(t_n + h,  y_n + Ah)
$$
$$
    y_{n+1} = y_n + (A + B)\frac{h}{2}
$$
This method does more computations, but compensates by converging faster than Euler, due to the corrections applied by evalutating twice.
#### RK4 Method
More sophisticated method calculating 4 steps each evaluation, correcting and converging even faster.
$$
    A = f(t_n, y_n)
$$
$$
    B = f(t_n + \frac{h}{2}, y_n +\frac{Ah}{2})
$$
$$
    C = f(t_n + \frac{h}{2}, y_n+ \frac{Bh}{2})
$$
$$
    D = f(t_n + h, y_n + Ch)
$$
$$
    y_{n+1} =  y_n + (A + 2B +  2C + D)\frac{h}{6}
$$
#### Primitve Adaptive Method
An Euler Method in its essence, but instead of a constant step size, it dynamically reduces or increases the step size to save on computing power. It does so by evaluating the Euler output and the Heun output and based on their difference adjusts the step. Let's call $y_e(t_n)$ and $y_h(t_n)$ for Euler and Heun respectively. If $\delta = |y_e(t_n) - y_h(t_n)|$, then we either $\delta > T_1 \Rightarrow h = h/2$ or $\delta < T_2 \Rightarrow h = 2h$, where $T_1, T_2$ are some arbitrary user set tolerance values.
## Description
Each of the methods has been tested on 3 different cases and compared to an analitycal/accurate numerical solution. A convergence and an error study have also been performed.
## Instructions
## Convergence
## Stability