import pygame
from sys import exit
import bodies
import c_engine
import random as rd

def check_if_int(prompt: str, deflaut: int):
    x = 5

    for _ in range(x):
        x -= 1
        try:
            response = input(prompt)
            if response == "none":
                break
            response = int(response)
            print(f"{response} entered.")
            return response
        except ValueError:
            print(f"Sorry please number a number. {x} more attempts.")
    
    print(f"Deflauting to {deflaut}")
    return deflaut

def settings():

    print("Welcome to my N-body Simulator :]")
    body_count = check_if_int("Enter number of bodies you want to simulate: ", 25)
    
    print("""
    1 - Normal Distribution
    """)
    menu_select = check_if_int("Select a distribution: ", 1)

    if menu_select == 1:
        normal_distribute(body_count)
    else:
        normal_distribute(body_count)

    return None

def normal_distribute(count: int):
    x_coordinates = []
    y_coordinates = []

    x_radius = check_if_int("Enter the radius of the normal distribution in pixels for X: ", 0.5 * bodies.screen_width)
    y_radius = check_if_int("Enter the radius of the normal distribution in pixels for Y: ", 0.5 * bodies.screen_height)

    for _ in range(int(count)):
        x_coordinates.append(rd.gauss(0, x_radius))
        y_coordinates.append((rd.gauss(0 , y_radius)))

    for _ in range(count):
        bodies.Body(100, rd.sample(x_coordinates, 1)[0], rd.sample(y_coordinates, 1)[0], (255, 255, 255), 0, 0)

def run_simulator():
    # Initializing Pygame Window
    pygame.init()
    screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
    pygame.display.set_caption("Simulator ツ")
    clock = pygame.time.Clock()

    running = True
    print("Running")

    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for _ in range(1):
            c_engine.calculate_force(0.1)

        bodies.Body.draw_all_bodies(screen)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

settings()
run_simulator()
