# ==============================
# ENERGY / SIMULATION PROBLEMS
# ==============================

# 1. PROBLEM: Potential energy is counted twice
#    Each pair is calculated twice:
#    A -> B and B -> A
#
#    SOLUTION:
#    Multiply the total potential energy by 0.5:
#
#    return np.sum(k_energy) + 0.5 * np.sum(p_energy)


# 2. PROBLEM: Force and potential energy use different equations
#    Acceleration currently uses:
#    r^2 + eps
#
#    Potential energy currently uses:
#    r + eps
#
#    These don't correspond to the same physical potential.
#
#    SOLUTION:
#    Make the force equation and potential-energy equation
#    mathematically consistent.


# 3. PROBLEM: Possible division by zero
#    If two bodies have exactly the same position:
#    r = 0
#
#    Then these become a problem:
#    x_dis / r
#    y_dis / r
#
#    SOLUTION:
#    Handle r == 0 before dividing by r.


# 4. PROBLEM: Collision detection doesn't stop the force calculation
#    When:
#
#    if r <= eps:
#        collide_with[i] = j
#
#    the code continues calculating the force afterward.
#
#    SOLUTION:
#    Decide how collisions should interact with the force calculation
#    and prevent invalid calculations when bodies overlap.


# 5. PROBLEM: Timestep may be too large
#    Current:
#
#    dt = 0.01
#
#    Large timesteps can cause numerical errors and energy drift,
#    especially when bodies get close together.
#
#    SOLUTION:
#    Test smaller values, for example:
#
#    dt = 0.001
#
#    Compare the energy behavior.


# 6. PROBLEM: Current integration method may cause energy drift
#    update_pos() uses the current acceleration to update position
#    and velocity.
#
#    SOLUTION:
#    Consider using a symplectic integrator such as:
#    - Leapfrog
#    - Velocity Verlet
#
#    These are generally better for long-term gravitational simulations.


# 7. PROBLEM: fastmath=True can make numerical debugging harder
#    Current:
#
#    @njit(parallel=True, fastmath=True)
#
#    fastmath allows numerical optimizations that can slightly
#    change floating-point calculations.
#
#    SOLUTION:
#    Temporarily remove fastmath while debugging:
#
#    @njit(parallel=True)
#
#    Add fastmath back after the physics is working correctly.


# 8. PROBLEM: Softening parameter needs to be reviewed
#    Current:
#
#    eps = bodies.b_radii * 2
#
#    and it is being added differently to r and r^2.
#
#    SOLUTION:
#    Choose a physically/mathematically consistent softening
#    method for both acceleration and potential energy.


# ==============================
# RECOMMENDED ORDER TO FIX
# ==============================

# 1. Fix potential-energy double counting
# 2. Disable collisions temporarily
# 3. Test with a smaller dt
# 4. Fix the force/potential consistency
# 5. Handle r == 0 safely
# 6. Improve the integration method
# 7. Test without fastmath
# 8. Revisit softening