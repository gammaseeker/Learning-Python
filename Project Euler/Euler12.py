def getNumDivisors(n):
    if n % 2 == 0: n = n/2
    div = 1
    ctr = 0
    while n % 2 == 0:
        ctr += 1
        n = n/2
    div = div * (ctr + 1)
    p = 3
    while n != 1:
        ctr = 0
        while n % p == 0:
            ctr += 1
            n = n/p
        div = div * (ctr + 1)
        p += 2
    return div

def triangle(factor):
    n = 1
    lnum, rnum = getNumDivisors(n), getNumDivisors(n+1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, getNumDivisors(n+1)
    return n

index = triangle(500)
triangle = (index * (index + 1)) / 2
print(triangle)
print(index)
