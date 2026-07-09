import pygame
from sys import exit

pygame.init()
sim_screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Simulator :)")
clock = pygame.time.Clock()

color = (255, 0, 0)
test_surface = pygame.Surface((100, 200))
center = (100, 100)
radius = 75

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.circle(sim_screen, color, center, radius)
    
    pygame.display.update()
    clock.tick(60)