import numpy
from numpy.random import uniform

a = 2
b = 1

def inside_ellipse(x, y):
    return x**2 / a**2 + y**2 / b**2 < 1

num_samples = int(10**5)
x = uniform(-2, 2, size=num_samples)
y = uniform(-2, 2, size=num_samples)
box_area = 4 * 4

area_mc = inside_ellipse(x, y).sum() / num_samples * box_area
area_exact = numpy.pi * a * b

print(area_exact)
print(area_mc)
