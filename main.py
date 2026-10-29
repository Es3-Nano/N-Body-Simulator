import time
import tkinter as tk
import numpy as np
import pygame
import random as rd

import bodies
import physics_engine
import control_panel

dt = 0.01
response_trys = 5
allowCollision = False
paused = False
softening = bodies.b_radii / 2
message = "Running simulation"
fast_foward_steps = 1

add_body_mode = delete_body_mode = False
need_force_refresh = True  

test_mode = False
log_file = None
LOG_EVERY = 1      # write a log entry every this many physics steps
LOG_BODIES = 5      # how many bodies to list in each entry
ARRAY_NAMES = ["mass", "x_pos", "y_pos", "x_vel", "y_vel", "acc_x", "acc_y"]
step_count = total_merges = 0

def start():
    global allowCollision, test_mode
    print("Welcome to my N-body Simulator :]")
    body_count = check_if_int("Enter number of bodies you want to simulate: ", 1000)
    collision_confrim = check_if_valid("Do you want collisions (y for yes, n for no)? ", "n", ["n", "y"])
    allowCollision = (collision_confrim == "y")

    test_confirm = check_if_valid("Do you want test mode with logs data to test_log.txt (y for yes, n for no)? ", "n", ["n", "y"])
    test_mode = (test_confirm == "y")

    intial_disk(body_count)

    if test_mode:
        start_test_log(body_count)

def check_if_int(prompt: str, deflaut: int, minimum: int = 0):
    for x in range(response_trys):
        try:
            response = int(input(prompt))
            if response < minimum:
                print(f"Please enter a whole number of at least {minimum}. {response_trys - x - 1} more attempts.")
                continue
            print(f"{response} entered.")
            return response
        except ValueError:
            print(f"Sorry please enter a whole number. {response_trys - x - 1} more attempts.")
    print(f"Deflauting to {deflaut}")
    return deflaut

def check_if_valid(prompt, deflaut, response_list: list):
    for x in range(response_trys):
        print(f"Options to enter are {', '.join(response_list)}")
        response = input(prompt).strip().lower()
        if response in response_list:
            return response
        print(f"Sorry that isn't one of the options. {response_trys - x - 1} more attempts.")
    print(f"Deflauting to {deflaut}")
    return deflaut

def intial_disk(body_count):
    radius = check_if_int("Enter the radius of the normal distribution in pixels: ", int(0.5 * min(bodies.screen_width, bodies.screen_height)), minimum=1)
    r = np.random.uniform(0, radius, body_count)
    theta = np.random.uniform(0, 2 * np.pi, body_count)
    x_coordinates = r * np.cos(theta)
    y_coordinates = r * np.sin(theta)

    mass_request = check_if_valid("Do you want randon masses (r) or same mass (s) for all bodies? ", "s", ["s", "r"])

    if mass_request == "s":
        mass_select = check_if_int("Enter the mass you want for all bobies: ", 100, minimum=1)
        for x, y in zip(x_coordinates, y_coordinates):
            bodies.create_body(mass_select, x, y)

    elif mass_request == "r":
        lowest_mass = check_if_int("Enter the lowest mass you want for any body: ", 100, minimum=1)
        highest_mass = check_if_int("Enter the highest mass you want for any body: ", 1000, minimum=1)
        if lowest_mass > highest_mass:
            print("Lowest was higher than highest, swapping them.")
            lowest_mass, highest_mass = highest_mass, lowest_mass
        mass_range = [rd.randint(lowest_mass, highest_mass) for _ in range(body_count)]
        for m, x, y in zip(mass_range, x_coordinates, y_coordinates):
            bodies.create_body(m, x, y)

def toggle_pause():
    global paused, message
    paused = not paused
    message = "Simulation paused" if paused else "Running simulation"

def enter_add_body_mode():
    global add_body_mode, delete_body_mode, message
    add_body_mode = True
    delete_body_mode = False
    message = "Click to place new body"

def enter_delete_body_mode():
    global add_body_mode, delete_body_mode, message
    delete_body_mode = True
    add_body_mode = False
    message = "Click a body to delete"

def clear_body_modes():
    global add_body_mode, delete_body_mode, message
    add_body_mode = False
    delete_body_mode = False
    message = "Running simulation" if not paused else "Simulation paused"

def add_body(m, x, y, xv, yv):
    global need_force_refresh
    bodies.create_body(m, x, y, xv, yv)
    need_force_refresh = True

def set_dt(value):
    global dt
    dt = float(value)

def set_fast_forward_steps(value):
    global fast_foward_steps
    fast_foward_steps = int(value)

def set_softening(value):
    global softening
    softening = float(value)

def compute_forces():
    return physics_engine.calculate_force(softening, bodies.mass, bodies.x_pos,bodies.y_pos, bodies.acc_x, bodies.acc_y)

def refresh_forces():
    global need_force_refresh
    compute_forces()
    need_force_refresh = False

def merge_collisions(collide_with):
    # Merges overlapping pairs, deletes the absorbed bodies and then it returns how many were merged.
    processed = set()
    dead = []
    for i in np.flatnonzero(collide_with != -1):
        i = int(i)
        j = int(collide_with[i])
        if i in processed or j in processed:
            continue
        bodies.collision(i, j)
        processed.add(i)
        processed.add(j)
        dead.append(j)

    dead_list = np.array(dead, dtype=np.int64)
    if len(dead_list) > 0:
        bodies.delete_body(dead_list)
    return len(dead_list)

def physics_step():
    global step_count, total_merges

    if need_force_refresh:
        refresh_forces()

    bodies.kick(dt)
    bodies.drift(dt)
    collide_with = compute_forces()

    if allowCollision:
        merged = merge_collisions(collide_with)
        total_merges += merged
        if merged > 0:
            compute_forces()

    bodies.kick(dt)
    step_count += 1

    if test_mode and step_count % LOG_EVERY == 0:
        log_step()

def start_test_log(body_count):
    global log_file
    log_file = open("test_log.txt", "w")
    log_file.write(f"Test log, started {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write(f"bodies asked for: {body_count} | collisions: {allowCollision} | dt: {dt} | softening: {softening}\n")
    log_file.write(f"logging every {LOG_EVERY} steps, first {LOG_BODIES} bodies listed\n\n")
    log_file.write("Array info at start:\n")
    for name in ARRAY_NAMES:
        arr = getattr(bodies, name)
        log_file.write(f"  {name}: dtype={arr.dtype} shape={arr.shape}\n")
    log_file.flush()

def log_step():
    n = bodies.number_of_bodies
    f = log_file
    f.write(f"\n--- step {step_count} | bodies {n} | merges so far {total_merges} | dt {dt} | softening {softening} ---\n")

    lengths = {len(getattr(bodies, name)) for name in ARRAY_NAMES}
    if lengths != {n}:
        f.write(f"WARNING: array lengths {lengths} don't match body count {n}\n")
    if n == 0:
        f.flush()
        return

    for name in ("acc_x", "acc_y"):
        arr = getattr(bodies, name)
        f.write(f"{name}: min={arr.min():.4e} max={arr.max():.4e} mean={arr.mean():.4e}\n")
    if np.isnan(bodies.acc_x).any() or np.isnan(bodies.acc_y).any():
        f.write("WARNING: NaN in acceleration\n")

    # total momentum should stay roughly constant (sum of mass * velocity)
    f.write(f"momentum: px={np.sum(bodies.mass * bodies.x_vel):.6e} py={np.sum(bodies.mass * bodies.y_vel):.6e}\n")

    f.write("i, mass, x, y, vx, vy, ax, ay\n")
    for i in range(min(n, LOG_BODIES)):
        f.write(f"{i}, {bodies.mass[i]:.2f}, {bodies.x_pos[i]:.3f}, {bodies.y_pos[i]:.3f}, "
                f"{bodies.x_vel[i]:.4e}, {bodies.y_vel[i]:.4e}, {bodies.acc_x[i]:.4e}, {bodies.acc_y[i]:.4e}\n")
    f.flush()

def pygame_events():
    global need_force_refresh, root
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            toggle_pause()

        if event.type == pygame.MOUSEBUTTONDOWN and add_body_mode:
            control_panel.open_add_body_popup(root, event.pos, add_body)
            clear_body_modes()

        if event.type == pygame.MOUSEBUTTONDOWN and delete_body_mode:
            if bodies.number_of_bodies == 0:
                clear_body_modes()
                continue
            click_x, click_y = event.pos
            distances = np.sqrt((bodies.x_pos - click_x) ** 2 + (bodies.y_pos - click_y) ** 2)
            nearest = np.argmin(distances)

            if distances[nearest] <= bodies.b_radii * 3:
                bodies.delete_body(nearest)
                need_force_refresh = True
            clear_body_modes()

def run_simulator():
    global need_force_refresh
    pygame.init()
    screen = pygame.display.set_mode((bodies.screen_width, bodies.screen_height))
    root, fps_label, num_bodies_label, physics_time_label, _, message_label = control_panel.control_panel(toggle_pause, set_dt, set_softening, set_fast_forward_steps, enter_add_body_mode, enter_delete_body_mode)
    pygame.display.set_caption("My Simulator ツ")
    clock = pygame.time.Clock()

    refresh_forces()    # it calculates initial acceleration for numerical integration
    if test_mode:
        log_step()

    running = True
    while running:
        screen.fill((0, 0, 0))
        pygame_events(root)
        t0 = time.perf_counter()

        if not paused:
            for _ in range(fast_foward_steps):
                physics_step()
        physics_time = time.perf_counter() - t0

        bodies.draw_all_bodies(screen)
        pygame.display.update()

        try:
            root.update()
            clock.tick(60)
            fps = clock.get_fps()
            control_panel.update_control_panel(fps, bodies.number_of_bodies, physics_time, fps_label, num_bodies_label, physics_time_label, message_label, message)
        except tk.TclError:
            running = False

    pygame.quit()
    try:
        root.destroy()
    except tk.TclError:
        pass
    if log_file:
        log_file.close()

if __name__ == "__main__":
    start()
    run_simulator()