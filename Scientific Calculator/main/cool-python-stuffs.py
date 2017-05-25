import math

def calcSin(x, c, n):
    sum = 0
    for i in range (0, math.ceil(n/2)):
        sum += ((-1)**i)*((x-c)**(2*i+1))/math.factorial(2*i+1)
    return sum

def calcLn(x, c, n):
    if(x < 1 or c < 1):
        return "Enter a number between the range of 1 to infinity."
    else:
        sum = math.log(c)
        for i in range (1, n+1):
            sum += (((-1)**(i+1))*((x-c)**i)/(i*(c**i)))
    return sum

def calcE(x, c, n):
    sum = 0
    for i in range (0, n+1):
        sum += ((x-c)**i)/math.factorial(i)
    return sum
         

print(calcSin(math.pi, 0, 5))
print(calcLn(3, 2, 3))
print(calcE(5, 0, 3))
