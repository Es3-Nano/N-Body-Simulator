import pygame
from sys import exit

y_pos = 50
flip_state = False

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

while True:
    if flip_state == False:
        y_pos += 1
    elif flip_state == True:
        y_pos -=1

    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.draw.circle(screen, (255, 0, 0), (400, y_pos), 20)

    if 380 <= y_pos:
        flip_state = True
    elif 20 >= y_pos:
        flip_state = False
    
    pygame.display.update()
    clock.tick(60)