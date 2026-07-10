import pygame
from sys import exit

y_pos = 0
flip_state = False
vel = 0
dt = 0.1
acc = 1

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    y_pos += vel * dt + 0.5 * acc * dt ** 2
    vel += acc * dt

    pygame.draw.circle(screen, (255, 0, 0), (400, y_pos), 20)
    print(vel)

    pygame.display.update()
    clock.tick(120)