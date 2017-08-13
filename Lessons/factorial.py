#Python mad good with numbers
def main():
    num = eval(input("Enter number for factorial: "))
    print(str(num) + "! =", factorial(num))

def factorial(num):
    if(num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num - 1)

main()