import math
def isPrime(n):
    if n > 2 and n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True

def getSum(limit):
    sum = 0
    for i in range(2, limit):
        if isPrime(i):
            sum += i
    
    return sum

print(getSum(2000000))
