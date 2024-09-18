from matplotlib import pyplot
import numpy

# time step
dt = 0.01


# spring bob mass
mass = 1000 # kg

# spring constant
k = 100

def total_force(x):
    return - k * x

def update_explicit(x, vel, force, dt):
    # a = f / m
    acc = force / mass
    new_pos = x + vx * dt
    new_vel = vx + acc * dt
    return new_pos, new_vel

def update_implicit(x, vel, force, dt):
    # a = f / m
    acc = force / mass
    new_vel = vx + acc * dt
    new_pos = x + new_vel * dt
    return new_pos, new_vel

pyplot.figure()

for label, update in zip(['Explicit', 'Implicit'],
                         [update_explicit, update_implicit]):

    x = 50
    vx = 0
    time = 0
    iteration = 0

    times = []
    posx = []

    while iteration < 40000:
        posx.append(x)
        times.append(time)

        force = total_force(x)
        x, vx = update(x, vx, force, dt)
        time += dt
        iteration += 1
        print(iteration, time, x, vx, force)

    pyplot.plot(times, posx, label=label)

pyplot.legend()
pyplot.xlabel('Time')
pyplot.ylabel('X displacement')
pyplot.show()
