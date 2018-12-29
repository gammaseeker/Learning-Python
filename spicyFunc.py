import math
from functools import reduce

def area(r):
    return math.pi * (r**2)

radii = [2, 5, 71, 0.3, 10]
a = map(area, radii)
print(list(a))

temps = [("Berlin", 29), ("Cairo", 36)]
c_to_f = lambda data: (data[0], (9/5)*data[1] + 32)
print(list(map(c_to_f, temps)))

# Multiply all numbers in a list
data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
multiplier = lambda x, y: x * y
print(reduce(multiplier, data))
