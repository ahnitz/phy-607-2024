import numpy.random
from matplotlib import pyplot as plt

size = int(1e9)

a = 2
b = 5
delta_b = 0.0001
sizes = numpy.arange(4, 9, .1)
sizes = 10 ** sizes
#sizes = [1e4, 1e5, 1e6, 1e7, 1e8, 1e9]
ans = []

a1 = []
a2 = []

for size in sizes:
    x = numpy.random.uniform(-a, a, size=int(size))
    y = numpy.random.uniform(-b, b, size=int(size))

    inside_outer = x**2 / (a + delta_b)**2 + y**2 / (b + delta_b)**2 < 1
    outer_area = a * b * 4 * inside_outer.sum() / len(inside_outer)

    inside_inner= x**2 / (a - delta_b)**2 + y**2 / (b - delta_b)**2 < 1
    inner_area = a * b * 4 * inside_inner.sum() / len(inside_inner)

    c = (outer_area - inner_area) / delta_b / 2.0
    print(c)
    ans.append(c)
    a1.append(outer_area)
    a2.append(inner_area)

plt.figure()
plt.plot(sizes, a1)
plt.xscale('log')
plt.show()

plt.figure()
plt.plot(sizes, a2)
plt.xscale('log')
plt.show()


plt.figure()
plt.plot(sizes, ans)
plt.xscale('log')
plt.show()

