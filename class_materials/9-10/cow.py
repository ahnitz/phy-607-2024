from matplotlib import pyplot
import numpy

# time step
dt = 0.001

# local gravitational constant
g = 9.81

# cow mass
mass = 1000 # kg

# drag constant
drag = 0.0
# drag = 4.0

def sign(x):
    if x > 0:
        return 1
    else:
        return -1

def total_force(vel):
    vx, vy = vel
    f_g = (0, -mass * g)
    f_w = (- drag * vx ** 2.0 * sign(vx),
           - drag * vy ** 2.0 * sign(vy),
           )
    total_f = (f_g[0] + f_w[0], f_g[1] + f_w[1])
    return total_f

def update(pos, vel, force, dt):
    (x, y), (vx, vy) = pos, vel
    # a = f / m
    acc = (force[0] / mass, force[1] / mass)
    new_pos = (x + vx * dt, y + vy * dt)
    new_vel = (vx + acc[0] * dt, vy + acc[1] * dt)
    return new_pos, new_vel
    
def energy(pos, vel):
    energy_potential = mass * (pos[1] * g)
    energy_kinetic = mass * (0.5 * (vel[0] ** 2.0 + vel[1] ** 2.0)) 
    return energy_potential, energy_kinetic
    
x = 0
y = 1000 # meters
time = 0
vx = 1 # meter / sec
vy = 100 # meter / sec

pos = (x, y)
vel = (vx, vy)

iteration = 0

times = []
posx = []
posy = []

energy_pot = []
energy_kin = []

while pos[1] > 0:
    posx.append(pos[0])
    posy.append(pos[1])
    times.append(time)
    
    p, k = energy(pos, vel)
    energy_pot.append(p)
    energy_kin.append(k)

    force = total_force(vel)
    pos, vel = update(pos, vel, force, dt)
    time += dt
    iteration += 1
    print(iteration, time, pos, vel, force)

t = numpy.arange(0, times[-1], .001)
ana_posy = - 1/2 * g * t**2.0 + vy * t + y
ana_posx = vx * t + x

pyplot.figure()
pyplot.plot(ana_posx, ana_posy, label='analytic [drag free]', linestyle='dashed')
pyplot.plot(posx, posy, label='numerical [euler]', linestyle='dotted')
pyplot.xlabel('X position [m]')
pyplot.ylabel('Y position [m]')
pyplot.legend()
pyplot.show()


pyplot.figure()
energy_pot = numpy.array(energy_pot)
energy_kin = numpy.array(energy_kin) 
pyplot.plot(times, energy_pot, label='Potential Energy')
pyplot.plot(times, energy_kin, label='Kinetic Energy')
pyplot.plot(times, energy_pot + energy_kin, label='Total Energy')
pyplot.legend()
pyplot.show()
