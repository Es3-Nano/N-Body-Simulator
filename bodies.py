import pygame

class Body:
    number_of_bodies = 0
    all_bodies = []

    def __init__(self, mass, x_pos, y_pos, color=tuple):  
        self.mass = mass
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = 0
        self.y_vel = 0
        self.radius = 10
        self.color = color
        Body.number_of_bodies += 1
        self.all_bodies.append(self)

    def draw_body(self, surface):
        pygame.draw.circle(surface, self.color, (self.x_pos, self.y_pos) , self.radius)