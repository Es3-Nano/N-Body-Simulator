import bodies
import math

# G = 1
eps = 1

def calculate_force(time_step):
    for p1 in bodies.Body.all_bodies:
        x_dis = 0
        y_dis = 0
        acc_mag = 0
        acc_x = 0
        acc_y = 0

        for p2 in bodies.Body.all_bodies:
            
            if p1 == p2:
                continue
        
            x_dis = p2.x_pos - p1.x_pos
            y_dis = p2.y_pos - p1.y_pos
            r = math.sqrt((x_dis ** 2) + (y_dis ** 2)) + eps
            acc_mag = (p2.mass) / ((r ** 2))
            acc_x += acc_mag * (x_dis / r)
            acc_y += acc_mag * (y_dis / r)

    
        p1.update_pos(time_step, acc_x, acc_y)
