print("Hello, World!")
print(2 + 3)
print("2 + 3 =", 2 + 3)
def hello():
    print("Hello")
    print("Computers are fun!")

hello()

def greet(person):
    print("Hello", person)
    print("How are you?")

greet("Joey")
greet("Prodigy")

def chaos():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)
chaos()