import pygame
from sys import exit
import bodies

screen_width = 800
screen_height = 400

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

planet_1 = bodies.Body(1000, 200, 200, (255, 0, 0))
planet_2 = bodies.Body(5000, 600, 200, (0, 255, 0))
planet_3 = bodies.Body(2000, 400, 200, (0, 0, 255))

def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        bodies.Body.draw_all_bodies(screen)

        pygame.display.update()
        clock.tick(60)

run_simulator()

# y_pos += vel * dt + 0.5 * acc * dt ** 2
# vel += acc * dt