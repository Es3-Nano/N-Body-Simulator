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

planet_1 = bodies.Body(100, 0, -300, (255, 0, 255), -0.5)
planet_2 = bodies.Body(100, 0, 300, (255, 255, 0), 0.5)
planet_3 = bodies.Body(100, 300, 0, (0, 255, 255), 0, 0.5)
planet_4 = bodies.Body(100, -300, 0, (255, 255, 255), 0, -0.5)
planet_5 = bodies.Body(1000, 0, 0, (0, 102, 204))

def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        bodies.Body.draw_all_bodies(screen)
        c_engine.calculate_force()

        pygame.display.update()
        clock.tick(120)

run_simulator()
