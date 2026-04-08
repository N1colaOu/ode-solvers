import numpy as np

def get_sol(t_start, t_end, h, y0, f):
    def y_n1(tn1, yn):
        res = newtons_method(yn, tn1, yn)
        if res != None:
            res = newtons_method(yn, tn1, yn)
        return res
    def g(x, k, c, h):
        return x - h*f(k, x) - c
    def dg(x, k, h):
        return 1 - f(k, x) + f(k, x-h)
    def newtons_method(x0, tn1, yn, max_iterations = 20, tolerance = 1e-5, epsilon = 1e-5): #typical Newton-Raphson method 
        for _ in range(max_iterations):       
            y = g(x0, tn1, yn, h)        
            y_prime = dg(x0, tn1, h)   
            if abs(y_prime) < epsilon: #check if divide by too little              
                break 
            x1 = x0 - y / y_prime           
            if abs(x1 - x0) <= tolerance:  #check if we are close enough to exit
                return x1            
            x0 = x1                       
        return None  

    t_span = np.abs(t_end - t_start)
    n = int(t_span/h)
    t = np.linspace(t_start, t_end, n)
    y = np.zeros(n, dtype=float)
    y[0] = y0
    for i in range(n-1):
        y[i+1] = y_n1(t[i], y[i])
    return y