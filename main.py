import pygame
from sys import exit
import bodies
import c_engine

screen_width = 1280
screen_height = 720

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

core = bodies.Body(10000, 0, 0, (255, 220, 50), 0, 0)

planet_1 = bodies.Body(80, 200, 0, (255, 0, 0), 0, -0.5)
planet_2 = bodies.Body(80, -200, 0, (0, 255, 0), 0, 0.5)

planet_3 = bodies.Body(60, 0, 350, (0, 0.500, 255), 0.5, 0)
planet_4 = bodies.Body(60, 0, -350, (255, 0, 255), -0.5, 0)

planet_5 = bodies.Body(40, 450, 200, (255, 255, 255), -0.5, 0.5)
planet_6 = bodies.Body(40, -450, -200, (255, 120, 0), 0.5, -0.5)

def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for l in range(1000):
            c_engine.calculate_force(0.01)

        bodies.Body.draw_all_bodies(screen)

        pygame.display.update()
        clock.tick(240)

run_simulator()
