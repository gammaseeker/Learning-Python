#Joey Jiemjitpolchai
import math
def isPrime2(num):
    if(num < 2):
        return False
    if(num ==2):
        return True
    if(num%2==0):
        return False
    ctr = 3
    while(ctr**2 <= num):
        if(num % ctr == 0):
            return False
        else:
            ctr += 2
    return True

def isPrime(n):
    for i in range(2, round(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
primeNum = 1
num = 1
while(primeNum < 10001):
    num += 2
    if(isPrime(num)):
        primeNum += 1

print(num)

upper = 10001
ctr = 1
list1 = [2]
while(len(list1) < upper):
    ctr += 2
    i = 0
    primeBool = True
    while(list1[i]**2 <= ctr):
        if(ctr % list1[i] == 0):
            primeBool = False
            break
        i += 1
    if(primeBool):
        list1.append(ctr)
print(ctr)
