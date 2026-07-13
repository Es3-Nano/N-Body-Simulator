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

black_hole = bodies.Body(30000, 0, 0, (40, 40, 40), 0, 0)

star_1 = bodies.Body(50, 150, 0, (255,255,255), 0, -5.5)
star_2 = bodies.Body(50, 250, 50, (255,100,100), -1, -4.8)
star_3 = bodies.Body(50, 350, 100, (100,255,255), -1.5, -4)

star_4 = bodies.Body(50, -150, 0, (255,255,0), 0, 5.5)
star_5 = bodies.Body(50, -250, -50, (255,0,255), 1, 4.8)
star_6 = bodies.Body(50, -350, -100, (100,255,100), 1.5, 4)

def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for l in range(100):
            c_engine.calculate_force(0.01)

        bodies.Body.draw_all_bodies(screen)

        pygame.display.update()
        clock.tick(240)

run_simulator()
