import numpy as np
import bodies
from numba import njit

lowest_x, highest_x = np.min(bodies.x_pos), np.max(bodies.x_pos)
lowest_y, highest_y = np.min(bodies.y_pos), np.max(bodies.y_pos)

def create_root():
    mass = np.append(mass, 0)
    node_CoM_x = np.append(node_CoM_x, (highest_x + lowest_x)/2)
    node_CoM_y = np.append(node_CoM_y, (highest_y + lowest_y)/2)
    node_upperx = np.append(node_upperx, highest_x)
    node_lowerx = np.append(node_lowerx, lowest_x)
    node_uppery = np.append(node_uppery, highest_y)
    node_lowery = np.append(node_lowery, lowest_y)
    node_p_count = np.append(node_p_count, 0)

@njit
def insert_particle(x_pos, y_pos, radii):
    for i, (p1_x, p1_y) in enumerate(zip(x_pos, y_pos)):
        x_dis = y_dis = 0

    return c_status

node_mass = np.array([])
node_CoM_x = np.array([], dtype='d')
node_CoM_y = np.array([], dtype='d')

node_upperx = np.array([], dtype='d')
node_lowerx = np.array([], dtype='d')
node_uppery = np.array([], dtype='d')
node_lowery = np.array([], dtype='d')

node_p_count = np.array([], dtype='u2')
is_node_parent = np.array([], dtype='b')