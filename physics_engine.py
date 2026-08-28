import math
import numpy as np
from numba import njit, prange, set_num_threads
import bodies

collisiosn_distance = bodies.b_radii * 2

@njit(parallel=True, fastmath=True)
def calculate_force(mass, x_pos, y_pos, acc_x, acc_y, potential_energy):
    num_particles = len(x_pos)
    collide_with = np.full(num_particles, -1, dtype=np.int64)

    for i in prange(num_particles):
        p1_x = x_pos[i]
        p1_y = y_pos[i]
        p1_m = mass[i]
        a_x = a_y = 0.0

        for j in range(num_particles):
            if i == j:
                continue

            p2_m = mass[j]
            p2_x = x_pos[j]
            p2_y = y_pos[j]
            dx = p2_x - p1_x
            dy = p2_y - p1_y

        r2 = dx * dx + dy * dy
        r = math.sqrt(r2)
        softening_length = r * 0.2
        softened_r2 = r2 + softening_length * softening_length
        softened_r = math.sqrt(softened_r2)
        denom = softened_r2 * softened_r

        if r <= collisiosn_distance / 2:
            collide_with[i] = j

        a_x += p2_m * dx / denom
        a_y += p2_m * dy / denom

        potential_energy[i] += -p1_m * p2_m / softened_r

        acc_x[i] = a_x
        acc_y[i] = a_y

    return collide_with