import pygame
import numpy as np

screen_width = 1280
screen_height = 720
number_of_bodies = 0
b_radii = 4

mass = np.array([], dtype='d')
x_pos = np.array([], dtype='d')
y_pos = np.array([], dtype='d')
x_vel = np.array([], dtype='d')
y_vel = np.array([], dtype='d')
acc_x = np.array([], dtype='d')
acc_y = np.array([], dtype='d')

circle = pygame.Surface((2 * b_radii, 2 * b_radii), pygame.SRCALPHA)
pygame.draw.circle(circle, (255, 255, 255), (b_radii, b_radii), b_radii)

def create_body(m, x_p, y_p, x_v=0, y_v=0):
    global mass, x_pos, y_pos, x_vel, y_vel, acc_x, acc_y, number_of_bodies
    mass = np.append(mass, m)
    x_pos = np.append(x_pos, x_p + screen_width / 2)
    y_pos = np.append(y_pos, screen_height / 2 - y_p)
    x_vel = np.append(x_vel, x_v)
    y_vel = np.append(y_vel, y_v)
    acc_x = np.append(acc_x, 0.0)
    acc_y = np.append(acc_y, 0.0)
    number_of_bodies += 1

def draw_all_bodies(surface):
    surface.blits([(circle, (x - b_radii, y - b_radii)) for x, y in zip(x_pos, y_pos)], doreturn=False)

def kick(dt):
    """Half step of velocity using the current acceleration."""
    global x_vel, y_vel
    x_vel += 0.5 * acc_x * dt
    y_vel += 0.5 * acc_y * dt

def drift(dt):
    """Move positions using the (half-kicked) velocity."""
    global x_pos, y_pos
    x_pos += x_vel * dt
    y_pos += y_vel * dt

def collision(b1, b2):
    global mass, x_pos, y_pos, x_vel, y_vel

    combined_mass = mass[b1] + mass[b2]
    x_vel[b1] = ((mass[b2] * x_vel[b2]) + (mass[b1] * x_vel[b1])) / combined_mass
    y_vel[b1] = ((mass[b2] * y_vel[b2]) + (mass[b1] * y_vel[b1])) / combined_mass
    x_pos[b1] = ((mass[b2] * x_pos[b2]) + (mass[b1] * x_pos[b1])) / combined_mass
    y_pos[b1] = ((mass[b2] * y_pos[b2]) + (mass[b1] * y_pos[b1])) / combined_mass
    mass[b1] = combined_mass

def delete_body(indices):
    """Delete one index or an array of indices in one go."""
    global mass, x_pos, y_pos, x_vel, y_vel, acc_x, acc_y, number_of_bodies

    mass = np.delete(mass, indices)
    x_pos = np.delete(x_pos, indices)
    y_pos = np.delete(y_pos, indices)
    x_vel = np.delete(x_vel, indices)
    y_vel = np.delete(y_vel, indices)
    acc_x = np.delete(acc_x, indices)
    acc_y = np.delete(acc_y, indices)
    number_of_bodies = len(mass)