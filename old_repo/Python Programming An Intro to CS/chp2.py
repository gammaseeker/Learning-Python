def convert():
    celsius = eval(input("What is the Celsius temperature?")) # eval() interprets string as code
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit")

convert()

print(3 + 4)
print(3, 4, 3 + 4)
print()
print("The answer is", 3 + 4)

myVar = 0
print(myVar)
myVar = 7
print(myVar)
name = input("Enter your name: ")
print(name)
ans = eval(input("Enter an expression: "))
print(ans)
x = 1
for i in range(10):
    x = 3.9 * x * (1-x)
    print(x)
for i in [0, 1, 2, 3]:
    print(i)
for odd in [1, 3, 5, 7, 9]:
    print(odd * odd)
print(list(range(10)))

def futureVal():
    print("This program will calculate the future value of your principle")
    principle = eval(input("Enter your principle: "))
    apr = eval(input("Enter the annual percentage rate: "))
    for i in range(10):
        principle = principle * (1 + apr)
    print("The value in 10 years is:", principle)