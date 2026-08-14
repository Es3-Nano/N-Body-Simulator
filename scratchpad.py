# import itertools
# import bodies
# import numpy as np
# import math

# eps = bodies.b_radii
# G = 1

# b_pairs = np.arange(bodies.number_of_bodies)
# print(b_pairs)

# def calculate_force(mass, x_pos, y_pos, acc_x, acc_y, radii, c_list, c_status):
#     for f_pair in itertools.combinations(b_pairs, r=2):
#         p1 = f_pair[0]
#         p2 = f_pair[1]

#         x_dis = x_pos[p2] - x_pos[p1]
#         y_dis = y_pos[p2] - y_pos[p1]
#         r = math.sqrt((x_dis ** 2) + (y_dis ** 2))

#         if r <= radii:
#             if not c_status:
#                 c_list[0] = p1
#                 c_list[1] = p2
#                 c_status = True
                            
#         f_mag = G ((mass[p1] * mass[p2]) / ((r ** 2) + (eps ** 2)))

#         acc_x[p1] += (f_mag / mass[p1]) * (x_dis / r)
#         acc_x[p2] += (f_mag / mass[p2]) * (x_dis / r)

#         acc_y[p1] += (f_mag / mass[p1]) * (y_dis / r)
#         acc_y[p2] += (f_mag / mass[p2]) * (y_dis / r)

#     return c_status

import numpy as np

mylist = np.zeros(10, dtype=np.int64)
print(mylist)