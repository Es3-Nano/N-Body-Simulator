import pygame
from sys import exit
import bodies
import c_engine

screen_width = 800
screen_height = 400

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

planet_1 = bodies.Body(100, 100, 300, (255, 0, 0), -0.1)
planet_2 = bodies.Body(10000000, 400, 100, (0, 255, 0), -0.1)
planet_3 = bodies.Body(50e8, 400, 200, (255, 255, 255), 0.1 )


def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        bodies.Body.draw_all_bodies(screen)
        c_engine.calculate_force()
        planet_2.show_acc()

        pygame.display.update()
        clock.tick(120)

run_simulator()