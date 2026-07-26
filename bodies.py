import pygame
import numpy as np

screen_width = 1280
screen_height = 720

mass = np.array([])
x_pos = np.array([])
y_pos = np.array([])
x_vel = np.array([])
y_vel = np.array([])
color = np.array([])
acc_x = np.array([])
acc_y = np.array([])
number_of_bodies = 0

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
    acc_x = np.zeros(number_of_bodies)
    acc_y = np.zeros(number_of_bodies)

def draw_all_bodies(surface):
    for a, b in zip(x_pos, y_pos):
        pygame.draw.circle(surface, (255, 255, 255), (a, b) , 5)

def update_pos(dt):
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    x_pos += (x_vel * dt) + (0.5 * acc_x * dt * dt)
    y_pos += (y_vel * dt) + (0.5 * acc_y * dt * dt)
    x_vel += acc_x * dt
    y_vel += acc_y * dt