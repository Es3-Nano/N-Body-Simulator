import pygame
import bodies
import physics_engine
import scipy.stats as stats
import random as rd
import time

dt = 0.001
response_trys = 5

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

    mu_x = 0
    mu_y = 0
    sp = 200
    mass_select = 0

    x_a, x_b = -x_radius / sp, x_radius / sp
    y_a, y_b = -y_radius / sp, y_radius / sp

    x_coordinates = stats.truncnorm.rvs(x_a, x_b, mu_x, sp, count).tolist()
    y_coordinates = stats.truncnorm.rvs(y_a, y_b, mu_y, sp, count).tolist()

    mass_request = check_if_valid("Do you want randon masses (r) or same mass (s) for all bodies: ", "s", ["s", "r"])
    
    if mass_request == "s":
        mass_select = check_if_int("Enter the mass you want for all bobies: ", 100)
        for x, y in zip(x_coordinates, y_coordinates):
            bodies.create_body(mass_select, x, y)

    elif mass_request == "r":
        lowest_mass = check_if_int("Enter the lowest mass you want for any body: ", 100)
        highest_mass = check_if_int("Enter the highest mass you want for any body: ", 1000)

        mass_range = [ rd.randint(lowest_mass, highest_mass) for _ in range(count) ]
        for m, x, y in zip(mass_range, x_coordinates, y_coordinates):
            bodies.create_body(m, x, y)

    bodies.intialize_acc()

def run_simulator():
    # Initializing Pygame Window
    pygame.init()
    screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
    pygame.display.set_caption("Simulator ツ")
    clock = pygame.time.Clock()

    running = True
    print("Running")

    while running:
        work_start = time.perf_counter()

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # C_Engine Part
        start = time.perf_counter()
        for _ in range(10):
            bodies.collision_list = physics_engine.calculate_force(
                bodies.mass, 
                bodies.x_pos, 
                bodies.y_pos, 
                bodies.acc_x, 
                bodies.acc_y, 
                bodies.b_radii, 
                bodies.collision_list)
            if len(bodies.collision_list) % 2 == 0 and len(bodies.collision_list) > 0:
                print(f"C: {len(bodies.collision_list)}")
                for _ in range(len(bodies.collision_list/2)):
                    pair_1 = 0
                    pair_2 = 1
                    bodies.collision(pair_1, pair_2, physics_engine.eps)
                    pair_1 += 2
                    pair_2 += 2
            bodies.update_pos(dt)
        physics_time = time.perf_counter() - start

        # Drawing the bodies
        start = time.perf_counter()
        bodies.draw_all_bodies(screen)
        draw_time = time.perf_counter() - start

        # Upadating the display
        start = time.perf_counter()
        pygame.display.update()
        display_time = time.perf_counter() - start

        # Time spent doing actual math
        work_time = time.perf_counter() - work_start

        # FPS
        tick_start = time.perf_counter()
        clock.tick(60)
        tick_time = time.perf_counter() - tick_start

        print(
            f"Physics: {physics_time:.6f}s | "
            f"Draw: {draw_time:.6f}s | "
            f"Display: {display_time:.6f}s | "
            f"Work: {work_time:.6f}s | "
            f"Tick: {tick_time:.6f}s  | "
            f"Number of Bodies: {bodies.number_of_bodies}"
        )

    pygame.quit()

settings()
run_simulator()
