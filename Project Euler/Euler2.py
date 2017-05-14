#Joey Jiemjitpolchai
def fib(n):
    if(n == 1):
        return 1
    elif(n == 2):
        return 1
    else:
        return fib(n-2) + fib(n-1)

sum = 0
ctr = 1
while fib(ctr) <= 4000000:
    if(fib(ctr) % 2 == 0):
        sum += fib(ctr)
    ctr+= 1
print(sum)
    
