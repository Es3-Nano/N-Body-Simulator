import pygame
from sys import exit
import bodies
import c_engine

# Initializing Pygame Window
pygame.init()
screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
pygame.display.set_caption("Simulator ツ")
clock = pygame.time.Clock()

black_hole = bodies.Body(100000, 0, 0, (40, 40, 40), 0, 0)

body_1 = bodies.Body(5, 120, 0, (255, 0, 0), 0, -28.87)
body_2 = bodies.Body(8, 160, 0, (0, 255, 0), 0, -25.00)
body_3 = bodies.Body(12, 210, 0, (0, 0, 255), 0, -21.82)
body_4 = bodies.Body(20, 270, 0, (255, 255, 0), 0, -19.25)
body_5 = bodies.Body(30, 340, 0, (255, 128, 0), 0, -17.14)
body_6 = bodies.Body(40, 420, 0, (255, 0, 255), 0, -15.43)
body_7 = bodies.Body(55, 510, 0, (0, 255, 255), 0, -14.00)
body_8 = bodies.Body(70, 620, 0, (128, 128, 128), 0, -12.70)

body_9 = bodies.Body(6, -150, 40, (128, 0, 255), 7, 24.5)
body_10 = bodies.Body(10, -220, -80, (255, 192, 203), -9, 21.0)
body_11 = bodies.Body(15, -300, 120, (0, 128, 0), -10, 17.5)
body_12 = bodies.Body(25, -390, -160, (0, 0, 128), 8, 14.5)
body_13 = bodies.Body(35, -500, 200, (128, 0, 0), -7, 12.0)
body_14 = bodies.Body(50, -650, -100, (0, 128, 128), 3, 11.0)

def run_simulator():
    while True:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        for l in range(100):
            c_engine.calculate_force(0.001)

        bodies.Body.draw_all_bodies(screen)

        pygame.display.update()
        clock.tick(60)

run_simulator()
