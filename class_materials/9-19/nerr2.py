

value = 0 - 0.33 + 0.33 == 0

print(value)

def subtract_adder(n):
    value = 0
    
    # subtract off n times
    for i in range(n):
        value -=  0.33
        
    # add n times
    for i in range(n):
        value += 0.33
    
    return value
    
value = subtract_adder(100000)

n ~ 10^20

print(value)
print(value == 0)

# 1e-16
# 1e-7-8

a = [1e-1, 1e-1, 1e-1, 1e-1, 3e-2, 3e-2, 2e-2]
