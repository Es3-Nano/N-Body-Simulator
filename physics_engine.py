import bodies
import math
from numba import jit

eps = 1

@jit(nopython=True) # Set "nopython" mode for best performance, equivalent to @njit
def calculate_force(dt):
    for i, (p1_x, p1_y) in enumerate(zip(bodies.x_pos, bodies.y_pos)):
        x_dis = y_dis = a_mag = 0

        for j, (p2_m, p2_x, p2_y) in enumerate(zip(bodies.mass, bodies.x_pos, bodies.y_pos)):
            if i == j:
                continue
        
            x_dis = p2_x - p1_x
            y_dis = p2_y - p1_y
            r = math.sqrt((x_dis ** 2) + (y_dis ** 2)) + eps            
            a_mag = (p2_m) / ((r ** 2))
            bodies.acc_x[i] += a_mag * (x_dis / r)
            bodies.acc_y[i] += a_mag * (y_dis / r)