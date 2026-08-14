import pygame
import bodies
import physics_engine
import scipy.stats as stats
import random as rd
import time

dt = 0.01
response_trys = 5
allowCollision = None

def start():
    global allowCollision
    print("Welcome to my N-body Simulator :]")
    body_count = check_if_int("Enter number of bodies you want to simulate: ", 1000)
    collision_confrim = check_if_valid("Do you want collisions (y for yes, n for no? ", "y", ["n", "y"])

    if collision_confrim == "y":
        allowCollision = True
    else:
        allowCollision = False

    normal_distribution(body_count)

def check_if_int(prompt: str, deflaut: int):

    for x in range(response_trys):
        try:
            response = input(prompt)

            if response == "deflaut" or response == "d":
                break

            response = int(response)
            print(f"{response} entered.")
            return response
        except ValueError:
            print(f"Sorry please number a number. {response_trys - x + 1} more attempts.")
    
    print(f"Deflauting to {deflaut}")
    return deflaut

def check_if_valid(prompt, deflaut, response_list: list):
    for x in range(response_trys):
        print(f"Options to enter are {', '.join(response_list)}")
        response = input(prompt).strip().lower()
        if response == "deflaut" or response == "d":
            break
        elif response in response_list:
            return response
        print(f"Sorry please number a number. {response_trys - x + 1} more attempts.")
    
    print(f"Deflauting to {deflaut}")
    return deflaut

def normal_distribution(body_count):    
    x_coordinates = []
    y_coordinates = []

    x_radius = check_if_int("Enter the radius of the normal distribution in pixels for X: ", 0.5 * bodies.screen_width)
    y_radius = check_if_int("Enter the radius of the normal distribution in pixels for Y: ", 0.5 * bodies.screen_height)

    mu_x = 0
    mu_y = 0
    sp = 30
    mass_select = None

    x_a, x_b = -x_radius / sp, x_radius / sp
    y_a, y_b = -y_radius / sp, y_radius / sp

    x_coordinates = stats.truncnorm.rvs(x_a, x_b, mu_x, sp, body_count)
    y_coordinates = stats.truncnorm.rvs(y_a, y_b, mu_y, sp, body_count)

    mass_request = check_if_valid("Do you want randon masses (r) or same mass (s) for all bodies? ", "s", ["s", "r"])
    
    if mass_request == "s":
        mass_select = check_if_int("Enter the mass you want for all bobies: ", 100)
        for x, y in zip(x_coordinates, y_coordinates):
            bodies.create_body(mass_select, x, y)

    elif mass_request == "r":
        lowest_mass = check_if_int("Enter the lowest mass you want for any body: ", 100)
        highest_mass = check_if_int("Enter the highest mass you want for any body: ", 1000)

        mass_range = [rd.randint(lowest_mass, highest_mass) for _ in range(body_count)]
        for m, x, y in zip(mass_range, x_coordinates, y_coordinates):
            bodies.create_body(m, x, y)

    bodies.intialize_acc()

def run_simulator():
    pygame.init()
    screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
    pygame.display.set_caption("Simulator ツ")
    clock = pygame.time.Clock()

    running = True
    collision_check = False
    print("Running")

    while running:

        frame_start = time.perf_counter()

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        start = time.perf_counter()
        for _ in range(1):
            collision_check = physics_engine.calculate_force(
                bodies.mass, 
                bodies.x_pos, 
                bodies.y_pos, 
                bodies.acc_x, 
                bodies.acc_y, 
                bodies.b_radii, 
                bodies.collision_list, 
                collision_check)

            if collision_check and allowCollision and len(bodies.collision_list) >= 2:
                bodies.collision(
                    bodies.collision_list[0],
                    bodies.collision_list[1],
                    physics_engine.eps)
                bodies.collision_list.clear()

            bodies.update_pos(dt)
        physics_time = time.perf_counter() - start

        bodies.draw_all_bodies(screen)
        pygame.display.update()

        # Total time for the frame
        frame_time = time.perf_counter() - frame_start

        # FPS
        clock.tick(30)
        fps = 1 / frame_time if frame_time > 0 else 0

        print(
            f"FPS: {fps:.2f} | "
            f"Bodies: {bodies.number_of_bodies} | "
            f"Frame Time: {frame_time:.6f}s | "
            f"Physics: {physics_time:.6f}s"
        )

    pygame.quit()

start()
run_simulator()
