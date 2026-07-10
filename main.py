import pygame
from sys import exit

y_pos = 50
flip_state = False
vel = 0
dt = 0.1
acc = 4
radius = 20

screen_width = 800
screen_height = 400

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
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

    if y_pos >= screen_height - radius:
        vel = -(vel - 0.1 * vel)

    pygame.draw.circle(screen, (255, 0, 0), (400, y_pos), radius)
    print(vel)

    pygame.display.update()
    clock.tick(60)