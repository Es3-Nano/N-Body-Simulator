import pygame

screen_width = 1280
screen_height = 720

class Body:
    number_of_bodies = 0
    all_bodies = []

    def __init__(self,  mass, x_pos, y_pos, color: tuple, x_vel = 0, y_vel = 0):  
        self.mass = mass
        self.x_pos = x_pos + screen_width / 2
        self.y_pos = screen_height / 2 - y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = 5
        self.color = color
        Body.number_of_bodies += 1
        self.all_bodies.append(self)

    def update_pos(self, dt, acc_x, acc_y):
        self.x_pos += self.x_vel * dt + 0.5 * acc_x * dt * dt
        self.y_pos += self.y_vel * dt + 0.5 * acc_y * dt * dt

        self.x_vel += acc_x * dt
        self.y_vel += acc_y * dt
        
    @classmethod
    def draw_all_bodies(cls, surface):
        for b in cls.all_bodies:
            pygame.draw.circle(surface, b.color, (b.x_pos, b.y_pos) , b.radius)
