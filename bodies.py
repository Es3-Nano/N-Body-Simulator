import pygame
import numpy as np
import math

screen_width = 1280
screen_height = 720
number_of_bodies = 0
b_radii = 5

mass = np.array([])
x_pos = np.array([], dtype='d')
y_pos = np.array([], dtype='d')
x_vel = np.array([], dtype='d')
y_vel = np.array([], dtype='d')
color = np.array([])
acc_x = np.array([], dtype='d')
acc_y = np.array([], dtype='d')
collision_list = np.array([], dtype="u2")

def create_body(m, x_p, y_p, x_v = 0, y_v = 0):
    global mass
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    global number_of_bodies
    mass = np.append(mass, m)
    x_pos = np.append(x_pos, x_p + screen_width / 2)
    y_pos = np.append(y_pos, screen_height / 2 - y_p)
    x_vel = np.append(x_vel, x_v)
    y_vel = np.append(y_vel, y_v)
    number_of_bodies += 1

def intialize_acc():
    global acc_x
    global acc_y
    acc_x = np.zeros(number_of_bodies, dtype='d')
    acc_y = np.zeros(number_of_bodies, dtype='d')

def draw_all_bodies(surface):
    for a, b in zip(x_pos, y_pos):
        pygame.draw.circle(surface, (255, 255, 255), (a, b) , b_radii)

def update_pos(dt):
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    x_pos += (x_vel * dt) + (0.5 * acc_x * dt * dt)
    y_pos += (y_vel * dt) + (0.5 * acc_y * dt * dt)
    x_vel += acc_x * dt
    y_vel += acc_y * dt

def collision(b1, b2, eps):
    global mass
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    global acc_x
    global acc_y
    global number_of_bodies

    print(f"P1: {b1}")
    print(f"P2: {b2}")

    combined_mass = mass[b1] + mass[b2]
    x_vel[b1] = ((mass[b2] * x_vel[b2]) + (mass[b1] * x_vel[b1])) / combined_mass
    y_vel[b1] = ((mass[b2] * y_vel[b2]) + (mass[b1] * y_vel[b1])) / combined_mass
    x_pos[b1] = ((mass[b2] * x_pos[b2]) + (mass[b1] * x_pos[b1])) / combined_mass
    y_pos[b1] = ((mass[b2] * y_pos[b2]) + (mass[b1] * y_pos[b1])) / combined_mass
    mass[b1] = combined_mass

    for b3, (p3_m, p3_x, p3_y) in enumerate(zip(mass, x_pos, y_pos)):
        if b3 == b2 or b3 == b1:
            continue
    
        x_dis = p3_x - x_pos[b1]
        y_dis = p3_y - y_pos[b1]
        r = math.sqrt((x_dis ** 2) + (y_dis ** 2)) + eps
        a_mag = (p3_m) / ((r ** 2))
        acc_x[b1] += a_mag * (x_dis / r)
        acc_y[b1] += a_mag * (y_dis / r)

    mass = np.delete(mass, b2)
    x_pos = np.delete(x_pos, b2)
    y_pos = np.delete(y_pos, b2)
    x_vel = np.delete(x_vel, b2)
    y_vel = np.delete(y_vel, b2)
    acc_x = np.delete(acc_x, b2)
    acc_y = np.delete(acc_y, b2)
    number_of_bodies -= 1