import numpy as np
import time

def time_execution(func, size):
    start_time = time.time()
    func(size)
    end_time = time.time()
    return end_time - start_time

def python_addition(size):
    x = [i for i in range(size)]
    y = [i for i in range(size)]
    result = [x[i] + y[i] for i in range(size)]

def numpy_addition(size):
    x = np.arange(size)
    y = np.arange(size)
    result = x + y

# Example 2: Dot product
def python_dot_product(size):
    x = [i for i in range(size)]
    y = [i for i in range(size)]
    result = sum(x[i] * y[i] for i in range(size))

def numpy_dot_product(size):
    x = np.arange(size)
    y = np.arange(size)
    result = np.dot(x, y)

if __name__ == "__main__":
    # Timing the functions
    size = 1

    print("Timing for element-wise addition:")
    python_time = time_execution(python_addition, size)
    numpy_time = time_execution(numpy_addition, size)
    print("Numpy is %2.1f X the performance of python" % (python_time / numpy_time))

    print("\nTiming for dot product:")
    python_time = time_execution(python_dot_product, size)
    numpy_time = time_execution(numpy_dot_product, size)
    print("Numpy is %2.1f X the performance of python" % (python_time / numpy_time))

