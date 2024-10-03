import numpy

from numpy.random import uniform
from matplotlib import pyplot as plt

a = 2
b = 1

def inside_ellipse(x, y):
    return x**2 / a**2 + y**2 / b**2 < 1

num_samples = int(10**5)
x = uniform(-2, 2, size=num_samples)
y = uniform(-2, 2, size=num_samples)
box_area = 4 * 4

inside = inside_ellipse(x, y)

area_mc = inside.sum() / num_samples * box_area
area_exact = numpy.pi * a * b


print(area_exact)
print(area_mc)

plt.figure()
plt.scatter(x, y, color='black')
plt.scatter(x[inside], y[inside], color='red')
plt.show()
