import numpy as np

def get_sol(t_start, t_end, h, y0, f, low = 1e-7, high = 1e-6, incr = 3, decr = 2): #if problems -> tweak tolerance

    y_list = [y0]
    t_list = [t_start]
    step = h
    counter = 1
    
    def get_perfect_step(step_to_find):
        assert low < high
        while True:
            A = f(t, y_list[-1])
            y1 = y_list[-1] + step_to_find * A
            y2_1= y_list[-1] + step_to_find/2 * A
            y2_2 = y2_1 + step_to_find/2 * f(t+step_to_find/2, y2_1)

            error = np.abs(y2_2 - y1) / np.abs(y1) #check difference between both iterations
            if error < low: #too close -> increase h
                step_to_find *= incr
                if step_to_find > 1:
                    break #too large
            elif error > high: #too far -> decrease h
                step_to_find /= decr
                if step_to_find < 1e-12:
                    break #too small
            else: #good enough -> keep h -> evaluate further
                break
        return step_to_find
    t = t_list[0]
    while t < t_end:
        if t + step > t_end:
            step = t_end - t
        step = get_perfect_step(step)        
        y_list.append(y_list[-1] + step*f(t, y_list[-1]))
        t += step
        t_list.append(t)
        counter += 1
    return y_list, t_list