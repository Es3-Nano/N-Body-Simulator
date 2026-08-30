import pygame
import bodies
import physics_engine
import control_panel
import numpy as np
import random as rd
import time

dt = 0.01
response_trys = 5
allowCollision = None
collision_processed_ids = set()

def start():
    global allowCollision
    print("Welcome to my N-body Simulator :]")
    body_count = check_if_int("Enter number of bodies you want to simulate: ", 1000)
    collision_confrim = check_if_valid("Do you want collisions (y for yes, n for no)? ", "n", ["n", "y"])

    if collision_confrim == "y":
        allowCollision = True
    elif collision_confrim == "n":
        allowCollision = False

    intial_disk(body_count)

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

def check_if_float(prompt: str, deflaut: float):

    for x in range(response_trys):
        try:
            response = input(prompt)

            if response == "deflaut" or response == "d":
                break

            response = float(response)
            print(f"{response} entered.")
            return response
        except ValueError:
            print(f"Sorry please number a float. {response_trys - x + 1} more attempts.")
    
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

def intial_disk(body_count):    
    x_coordinates = []
    y_coordinates = []

    radius = check_if_int("Enter the radius of the normal distribution in pixels: ", 0.5 * min(bodies.screen_width, bodies.screen_height))
    mass_select = None

    r = np.random.uniform(0, radius, body_count)
    theta = np.random.uniform(0, 2 * np.pi, body_count)

    x_coordinates = r * np.cos(theta)
    y_coordinates = r * np.sin(theta)

    mass_request = check_if_valid("Do you want randon masses (r) or same mass (s) for all bodies? ","s", ["s", "r"])

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

    bodies.intialize_arrays()

def run_simulator():
    pygame.init()
    screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
    root, fps_label, num_bodies_label, physics_time_label = control_panel.control_panel()
    pygame.display.set_caption("My Simulator ツ")
    clock = pygame.time.Clock()

    physics_engine.calculate_force(
        bodies.mass,
        bodies.x_pos,
        bodies.y_pos,
        bodies.acc_x,
        bodies.acc_y)
    bodies.old_acc_x = bodies.acc_x.copy()
    bodies.old_acc_y = bodies.acc_y.copy()

    running = True
    print("Running simulation...")

    while running:
        root.update()
        frame_start = time.perf_counter()

        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                root.destroy()
                running = False

        bodies.intialize_arrays()

        start = time.perf_counter()
        for _ in range(50):
            collide_with = physics_engine.calculate_force(
                bodies.mass,
                bodies.x_pos,
                bodies.y_pos,
                bodies.acc_x,
                bodies.acc_y)

            if allowCollision:
                for i, j in enumerate(collide_with):
                    if j == -1:
                        continue
                    if i in collision_processed_ids or j in collision_processed_ids:
                        continue

                    bodies.collision(i, j)
                    collision_processed_ids.add(i)
                    collision_processed_ids.add(j)
                    bodies.dead_list = np.append(bodies.dead_list, j)

                collision_processed_ids.clear()
                for i in sorted(bodies.dead_list, reverse=True):
                    if i != -1:
                        bodies.delete_body(i)

            bodies.update_pos(dt)
            bodies.old_acc_x = bodies.acc_x.copy()
            bodies.old_acc_y = bodies.acc_y.copy()

        physics_time = time.perf_counter() - start

        bodies.draw_all_bodies(screen)
        pygame.display.update()
        frame_time = time.perf_counter() - frame_start

        clock.tick(30)
        fps = 1 / frame_time if frame_time > 0 else 0
        control_panel.update_control_panel(fps, bodies.number_of_bodies, physics_time, fps_label, num_bodies_label, physics_time_label)

    pygame.quit()

start()
run_simulator()
