from matplotlib import pyplot as plt

def repeat_add_sub(x, n=100):
    """ Add and subtract the value from 0 n times
    """
    value = 0.0
    
    # subtract n times
    for i in range(n):
        value -= x
        
    # add n times
    for i in range(n):
        value += x
        
    return value


errs = []
sizes = [1, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]

for n in sizes:    
    v = repeat_add_sub(0.35, n=int(n))
    print(v, v==0)
    errs.append(v)
    
plt.plot(sizes, errs)
plt.show()



