import math
from numba import jit
import numpy as np

eps = 1

def calculate_force(mass, x_pos, y_pos, acc_x, acc_y, radii, c_list):
    for i, (p1_x, p1_y) in enumerate(zip(x_pos, y_pos)):
        x_dis = y_dis = a_mag = 0

        for j, (p2_m, p2_x, p2_y) in enumerate(zip(mass, x_pos, y_pos)):
            if i == j:
                continue
        
            x_dis = p2_x - p1_x
            y_dis = p2_y - p1_y
            r = math.sqrt((x_dis ** 2) + (y_dis ** 2)) + eps    

            if r <= radii:
                if i not in c_list and j not in c_list:
                    c_list = np.append(c_list, [i, j])
                             
            a_mag = (p2_m) / ((r ** 2))
            acc_x[i] += a_mag * (x_dis / r)
            acc_y[i] += a_mag * (y_dis / r)

    return c_list
