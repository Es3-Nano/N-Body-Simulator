import pygame

class Body:
    number_of_bodies = 0
    all_bodies = []

    def __init__(self, mass, x_pos, y_pos, color: tuple, x_vel = 0, y_vel = 0):  
        self.mass = mass
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.x_acc = 0
        self.y_acc = 0
        self.radius = 5
        self.color = color
        Body.number_of_bodies += 1
        self.all_bodies.append(self)

    def update_pos(self, dt, acc_x, acc_y = 0):
        self.x_vel += 0.5 * self.x_acc * dt
        self.x_pos += self.x_vel
        self.x_acc += acc_x
        self.x_vel += 0.5 * self.x_acc * dt

        self.y_vel += 0.5 * self.y_acc * dt
        self.y_pos += self.y_vel
        self.y_acc += acc_y
        self.y_vel += 0.5 * self.y_acc * dt

    def show_acc(self):
        print(self.y_acc)
        
    @classmethod
    def draw_all_bodies(cls, surface):
        for b in cls.all_bodies:
            pygame.draw.circle(surface, b.color, (b.x_pos, b.y_pos) , b.radius)