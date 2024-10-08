import numpy as np
from matplotlib import pyplot as plt
from num import time_execution, python_dot_product, numpy_dot_product

perf_fac = []
pows = np.arange(1, 8, .5)
for size_pow in pows:
    size = int(10 ** size_pow)
    t1 = time_execution(python_dot_product, size)
    t2 = time_execution(numpy_dot_product, size)
    print(t1, t2)
    perf_fac.append(t1 / t2)

plt.figure()
plt.plot(pows, perf_fac)
plt.xlabel("$Log_{10}$ Vector Size")
plt.ylabel("Relative Performance")
plt.show()
