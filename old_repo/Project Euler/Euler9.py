def pytha(a, b, c):
    if(a**2 + b**2 == c**2):
        return True
    return False

product = 0
for a in range(1, 1000):
    for b in range(a, 1000-a):
        c = 1000 - b - a
        if(pytha(a, b, c)):
            print(a*b*c)
            
