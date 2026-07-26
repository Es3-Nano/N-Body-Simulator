import pygame
import bodies
import c_engine
import scipy.stats as stats
import time

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
    y_radius = check_if_int("Enter the radius of the normal distribution in pixels for Y: ", 0.5 * bodies.screen_height) # If user types none the deflaut value is the second parameter

    mu_x = 0
    mu_y = 0
    sp = 200

    x_a, x_b = -x_radius / sp, x_radius / sp
    y_a, y_b = -y_radius / sp, y_radius / sp

    x_coordinates = stats.truncnorm.rvs(x_a, x_b, mu_x, sp, count).tolist()
    y_coordinates = stats.truncnorm.rvs(y_a, y_b, mu_y, sp, count).tolist()

    for x, y in zip(x_coordinates, y_coordinates):
        bodies.create_body(100, x, y)

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
            c_engine.calculate_force(0.01)
        physics_time = time.perf_counter() - start

        # Drawing
        start = time.perf_counter()
        bodies.draw_all_bodies(screen)
        draw_time = time.perf_counter() - start

        # Display update
        start = time.perf_counter()
        pygame.display.update()
        display_time = time.perf_counter() - start

        # Time spent doing actual work
        work_time = time.perf_counter() - work_start

        # FPS limiter
        tick_start = time.perf_counter()
        clock.tick(30)
        tick_time = time.perf_counter() - tick_start

        print(
            f"Physics: {physics_time:.6f}s | "
            f"Draw: {draw_time:.6f}s | "
            f"Display: {display_time:.6f}s | "
            f"Work: {work_time:.6f}s | "
            f"Tick: {tick_time:.6f}s"
        )

    pygame.quit()

settings()
run_simulator()
