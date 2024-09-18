a = int(1e9)
b = 0

for i in range(int(1e7)):
    b += 1e-4
a += b

print(a)
