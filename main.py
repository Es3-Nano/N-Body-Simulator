import pygame
from sys import exit

y_pos = 50

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

    y_pos += 1
    pygame.draw.circle(screen, (255, 0, 0), (400, y_pos), 20)
    
    pygame.display.update()
    clock.tick(60)