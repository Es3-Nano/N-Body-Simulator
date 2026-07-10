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
        self.x_acc = 0
        self.y_acc = 0
        self.radius = 10
        self.color = color
        Body.number_of_bodies += 1
        self.all_bodies.append(self)

    def update_acc(self, x_acc, y_acc = 0):
        self.x_acc += x_acc

    def show_acc(self):
        return self.x_acc
        

    @classmethod
    def draw_all_bodies(cls, surface):
        for b in cls.all_bodies:
            pygame.draw.circle(surface, b.color, (b.x_pos, b.y_pos) , b.radius)

planet_1 = Body(1000, 200, 200, (255, 0, 0))
planet_2 = Body(5000, 600, 200, (0, 255, 0))
planet_3 = Body(2000, 400, 200, (0, 0, 255))

print(planet_1)