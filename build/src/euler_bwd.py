def get_sol(t, y0, f, m_iter = 20, tol = 1e-9, eps = 1e-5):
    h = t[1] - t[0]
    def y_n1(tn1, yn):
        res = newtons_method(yn, tn1, yn)
        return res
    def g(x, k, c, h):
        return x - h*f(k, x) - c
    def dg(x, k, h):
        return 1 - f(k, x+h) + f(k, x) #use +h/ or /-h
    def newtons_method(x0, tn1, yn, max_iterations = m_iter, tolerance = tol, epsilon = eps): #typical Newton-Raphson method 
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

    y = [y0]
    for i in range(len(t)-1):
        y.append(y_n1(t[i+1], y[i]))
    return y