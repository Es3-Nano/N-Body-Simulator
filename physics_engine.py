import math
import numpy as np
from numba import njit, prange
import bodies

collisiosn_distance = bodies.b_radii * 2
epsilon =  bodies.b_radii/2

@njit(parallel=True, fastmath=True)
def calculate_force(mass, x_pos, y_pos, acc_x, acc_y):
    num_particles = len(x_pos)
    collide_with = np.full(num_particles, -1, dtype=np.int64)

    for i in prange(num_particles):
        p1_x = x_pos[i]
        p1_y = y_pos[i]
        a_x = a_y = 0.0

        for j in range(num_particles):
            if i == j:
                continue

            p2_m = mass[j]
            dx = x_pos[j] - p1_x
            dy = y_pos[j] - p1_y

            r2 = dx * dx + dy * dy
            r = math.sqrt(r2)
            denom = (r2 + epsilon ** 2) ** 1.5

            if r <= collisiosn_distance / 2:
                collide_with[i] = j

            a_x += p2_m * dx / denom
            a_y += p2_m * dy / denom

        acc_x[i] = a_x
        acc_y[i] = a_y

    return collide_with