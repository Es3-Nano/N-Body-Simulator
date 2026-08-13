import math
from numba import njit

eps = 0.1

@njit
def calculate_force(mass, x_pos, y_pos, acc_x, acc_y, radii, c_list, c_status):
    c_status = False
    for i, (p1_x, p1_y) in enumerate(zip(x_pos, y_pos)):
        x_dis = y_dis = a_mag = a_y = a_x = 0

        for j, (p2_m, p2_x, p2_y) in enumerate(zip(mass, x_pos, y_pos)):
            if i == j:
                continue
        
            x_dis = p2_x - p1_x
            y_dis = p2_y - p1_y
            r = math.sqrt((x_dis ** 2) + (y_dis ** 2)) + eps    

            if r <= radii:
                if not c_status:
                    c_list[0] = i
                    c_list[1] = j
                    c_status = True
                             
            a_mag = (p2_m) / ((r ** 2))
            a_x += a_mag * (x_dis / r)
            a_y += a_mag * (y_dis / r)

        acc_y[i] = a_y
        acc_x[i] = a_x

    return c_status
