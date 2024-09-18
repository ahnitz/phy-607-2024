

a = 1e15

b = a
for i in range(int(1e8)):
    b += .1    
    
print(a, b)

b = 0
for i in range(int(1e8)):
    b += .1    
b += a

print(a, b)
