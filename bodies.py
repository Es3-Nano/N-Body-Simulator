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

    @classmethod
    def draw_all_bodies(cls, surface):
        for b in cls.all_bodies:
            pygame.draw.circle(surface, b.color, (b.x_pos, b.y_pos) , b.radius)