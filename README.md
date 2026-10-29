# N-Body Simulator

A 2D gravitational N-body simulator built with **pygame** for rendering and **Numba** for fast, parallelized physics calculations. Bodies attract each other via Newtonian gravity, can optionally collide and merge, and the simulation is controllable in real time through a Tkinter side panel.

## Features

- **Direct-summation gravity** — every body's acceleration is computed from every other body (O(n²)) using a softened Newtonian force law, JIT-compiled and parallelized with Numba for performance.
- **Velocity Verlet integration** (kick-drift-kick form, one acceleration array) for stable position/velocity updates.
- **Initial disk distribution** — bodies are seeded within a circular (disk) region using a uniform radius/angle distribution.
- **Configurable masses** — choose a single fixed mass for all bodies, or a random mass within a range.
- **Optional collisions** — merges colliding bodies (conserving momentum and combined mass) and removes the absorbed body.
- **Test mode** — optional console prompt at startup that writes array info, acceleration stats, momentum and a few sample bodies to `test_log.txt` every 50 steps.
- **Live control panel** (Tkinter) with:
  - Play/pause toggle
  - Time step (`dt`) slider
  - Softening length slider
  - Fast-forward (steps-per-frame) slider
  - Add Body / Delete Body modes (click on the simulation window to place or remove a body)
  - FPS, body count, and physics-time readouts
- **Interactive editing** — add a new body (with custom mass and velocity) or delete an existing one by clicking directly in the simulation window.

## Requirements

- Python 3.8+
- [pygame](https://www.pygame.org/)
- [numpy](https://numpy.org/)
- [numba](https://numba.pydata.org/)
- `tkinter` (included with most standard Python installations)

Install the Python dependencies with:

```bash
pip install pygame numpy numba
```
Note: pygame or pygame-ce can both work

## Project Structure

| File                | Purpose                                                                 |
|---------------------|--------------------------------------------------------------------------|
| `main.py`           | Entry point — handles setup prompts, the pygame event/render loop, and wiring the control panel to the simulation state. |
| `bodies.py`         | Body state storage (positions, velocities, masses, accelerations as NumPy arrays) and operations: create, delete, merge (collide), draw, and the kick/drift integration steps. |
| `physics_engine.py` | Numba-accelerated gravitational force calculation and collision detection. |
| `control_panel.py`  | Tkinter-based control panel: sliders, buttons, labels, and the "add body" popup dialog. |

## Usage

Run the simulator from the command line:

```bash
python main.py
```

You'll be prompted in the terminal to configure the initial setup:

1. **Number of bodies** to simulate.
2. Whether to **enable collisions** (`y`/`n`).
3. Whether to enable **test mode** (`y`/`n`).
4. The **radius** of the initial disk distribution (in pixels).
5. Whether all bodies should share the **same mass** or use **random masses** within a range you specify.

After 5 invalid attempts a prompt falls back to its default value.

Once configured, two windows open:
- A **pygame window** showing the live simulation.
- A **Tkinter control panel** for adjusting parameters while it runs.

### Controls

| Action                  | How                                                    |
|--------------------------|--------------------------------------------------------|
| Pause / resume           | Spacebar, or the ▶ button in the control panel        |
| Adjust time step         | "Time Step" slider                                     |
| Adjust softening length  | "Softening" slider (prevents force singularities at close range) |
| Speed up simulation      | "Fast Forward Steps" slider (physics steps per rendered frame) |
| Add a body               | Click "Add Body ●", then click in the simulation window and enter mass/velocity |
| Delete a body            | Click "Delete Body ●", then click on a body in the simulation window |

## How It Works

- Body data (mass, position, velocity, acceleration) is stored in flat NumPy arrays for efficient vectorized updates.
- Each simulation step:
  1. `physics_engine.calculate_force` (called after the position update) computes pairwise gravitational accelerations (with a softening term to avoid divide-by-zero at short range) and flags any pairs within the collision distance.
  2. Each step is: half-step velocity update, move positions, recalculate acceleration at the new positions, half-step velocity update (velocity Verlet).
  3. If collisions are enabled, flagged pairs are merged via a mass-weighted average of position and velocity, the absorbed bodies are removed, and acceleration is recalculated.
- The "Fast Forward Steps" control lets you run multiple physics steps per rendered frame to speed up long-timescale simulations without sacrificing render smoothness.

## Performance

- Performance scales as O(n²) per step, so very large body counts (several thousand+) will slow down noticeably, even with Numba's parallelization.
- This project was developed and tuned with a target of **~5,000 bodies** in mind, on the following hardware:
  - CPU: Intel Core i7-14650HX (16+8 cores) @ 5.20 GHz
  - GPU: NVIDIA GeForce RTX 4060 Max-Q (Mobile)
  - RAM: 32 GB
  - OS: Ubuntu 24.04.5 LTS
- At lower body counts (a few hundred to low thousands), performance should be reasonable on most modern machines. As you approach the ~5,000-body range, expect a noticeable drop in FPS on less powerful hardware, since the force calculation is CPU-bound and scales quadratically.
- If you're on a less powerful machine, reduce the body count, increase the "Fast Forward Steps" setting sparingly, or accept a lower frame rate.

## Notes

- The screen resolution is fixed at 1280×720 (`bodies.screen_width` / `bodies.screen_height`); adjust these constants in `bodies.py` if you need a different window size.