import random
import bodies
import numpy as np

x_coordinates = []
y_coordinates = []

for _ in range(100):
    x_coordinates.append(random.gauss(5, 5))
    y_coordinates.append((random.gauss(5, 5)))


black_hole = bodies.Body(100000, 0, 0, (40, 40, 40), 0, 0)

body_1 = bodies.Body(5, 120, 0, (255, 0, 0), 0, -28.87)
body_2 = bodies.Body(8, 160, 0, (0, 255, 0), 0, -25.00)
body_3 = bodies.Body(12, 210, 0, (0, 0, 255), 0, -21.82)
body_4 = bodies.Body(20, 270, 0, (255, 255, 0), 0, -19.25)
body_5 = bodies.Body(30, 340, 0, (255, 128, 0), 0, -17.14)
body_6 = bodies.Body(40, 420, 0, (255, 0, 255), 0, -15.43)
body_7 = bodies.Body(55, 510, 0, (0, 255, 255), 0, -14.00)
body_8 = bodies.Body(70, 620, 0, (128, 128, 128), 0, -12.70)

body_9 = bodies.Body(6, -150, 40, (128, 0, 255), 7, 24.5)
body_10 = bodies.Body(10, -220, -80, (255, 192, 203), -9, 21.0)
body_11 = bodies.Body(15, -300, 120, (0, 128, 0), -10, 17.5)
body_12 = bodies.Body(25, -390, -160, (0, 0, 128), 8, 14.5)
body_13 = bodies.Body(35, -500, 200, (128, 0, 0), -7, 12.0)
body_14 = bodies.Body(50, -650, -100, (0, 128, 128), 3, 11.0)

###################################################################
mass = np.array([])
x_pos = np.array([])
y_pos = np.array([])
x_vel = np.array([])
y_vel = np.array([])
color = np.array([])
acc_x = np.array([])
acc_y = np.array([])

def create_body(m, x_p, y_p, x_v, y_v):
    mass = np.append(mass, m)
    x_pos = np.append(x_pos, x_p)
    y_pos = np.append(y_pos, y_p)
    x_vel = np.append(x_vel, x_v)
    y_vel = np.append(y_vel, y_v)

#for _ in zip(mass, x_pos, y_pos):
#    pygame.draw.circle(surface, (255, 255, 255), (x_pos, y_pos) , 5)

def update_pos(dt):
    x_pos += x_vel * dt + 0.5 * acc_x * dt * dt
    y_pos += y_vel * dt + 0.5 * acc_y * dt * dt

    x_vel += acc_x * dt
    y_vel += acc_y * dt