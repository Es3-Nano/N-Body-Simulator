import pygame
import numpy as np

screen_width = 1280
screen_height = 720
number_of_bodies = 0
b_radii = 3

mass = np.array([])
x_pos = np.array([], dtype='d')
y_pos = np.array([], dtype='d')
x_vel = np.array([], dtype='d')
y_vel = np.array([], dtype='d')
color = np.array([])
acc_x = np.array([], dtype='d')
acc_y = np.array([], dtype='d')
old_acc_x = np.array([], dtype='d')
old_acc_y = np.array([], dtype='d')
dead_list = np.array([], dtype='d')

circle = pygame.Surface((10, 10), pygame.SRCALPHA)
pygame.draw.circle(circle, (255, 255, 255), (5, 5), b_radii)

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

def draw_all_bodies(surface):
    for x, y in zip(x_pos, y_pos):
        surface.blit(circle, (x - b_radii, y - b_radii))

def intialize_arrays():
    global acc_x
    global acc_y
    global dead_list
    acc_x = np.zeros(number_of_bodies, dtype='d')
    acc_y = np.zeros(number_of_bodies, dtype='d')
    dead_list = np.full(number_of_bodies, -1, dtype=np.int64)

def update_pos(dt):
    global x_pos
    global y_pos
    global x_vel
    global y_vel

    x_pos += (x_vel * dt) + (0.5 * old_acc_x * dt ** 2)
    y_pos += (y_vel * dt) + (0.5 * old_acc_y * dt ** 2)
    x_vel += (old_acc_x + acc_x) * 0.5 * dt
    y_vel += (old_acc_y + acc_y) * 0.5 * dt

def collision(b1, b2):
    global mass
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    global number_of_bodies

    combined_mass = mass[b1] + mass[b2]
    x_vel[b1] = ((mass[b2] * x_vel[b2]) + (mass[b1] * x_vel[b1])) / combined_mass
    y_vel[b1] = ((mass[b2] * y_vel[b2]) + (mass[b1] * y_vel[b1])) / combined_mass
    x_pos[b1] = ((mass[b2] * x_pos[b2]) + (mass[b1] * x_pos[b1])) / combined_mass
    y_pos[b1] = ((mass[b2] * y_pos[b2]) + (mass[b1] * y_pos[b1])) / combined_mass
    mass[b1] = combined_mass

def delete_body(b2):
    global mass
    global x_pos
    global y_pos
    global x_vel
    global y_vel
    global acc_x
    global acc_y
    global old_acc_x
    global old_acc_y
    global number_of_bodies

    mass = np.delete(mass, b2)
    x_pos = np.delete(x_pos, b2)
    y_pos = np.delete(y_pos, b2)
    x_vel = np.delete(x_vel, b2)
    y_vel = np.delete(y_vel, b2)
    acc_x = np.delete(acc_x, b2)
    acc_y = np.delete(acc_y, b2)
    old_acc_x = np.delete(old_acc_x, b2)
    old_acc_y = np.delete(old_acc_y, b2)
    number_of_bodies -= 1