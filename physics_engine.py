import math
from numba import njit, prange
import bodies

eps = bodies.b_radii

@njit(parallel=True, fastmath=True)
def calculate_force(mass, x_pos, y_pos, acc_x, acc_y, radii, c_list, c_status):
    c_status = False
    num_particles = len(x_pos)

    for i in prange(num_particles):
        p1_x = x_pos[i]
        p1_y = y_pos[i]
        
        x_dis = y_dis = a_mag = a_y = a_x = 0

        for j in prange(num_particles):
            if i == j:
                continue

            p2_m = mass[j]
            p2_x = x_pos[j]
            p2_y = y_pos[j]
        
            x_dis = p2_x - p1_x
            y_dis = p2_y - p1_y
            r = math.sqrt((x_dis ** 2) + (y_dis ** 2))   

            if r <= radii and c_status == False:
                    c_list[0] = i
                    c_list[1] = j
                    c_status = True
                             
            a_mag = (p2_m) / ((r ** 2) + (eps))
            a_x += a_mag * (x_dis / r)
            a_y += a_mag * (y_dis / r)

        acc_y[i] = a_y
        acc_x[i] = a_x

    return c_status
