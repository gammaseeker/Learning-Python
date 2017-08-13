def main():
    print("This program is designed to predict the future value of an investment.")
    principle = eval(input("Please input the principle amount: $"))
    apr = eval(input("Please provide the annual percentage rate: "))
    apr = apr/10
    for i in range(10):
        principle = principle * (1 + apr)
    print("In ten years your investment will be worth:$", principle)

def alt():
    print("This program is designed to predict the future value of an investment.")
    principle = eval(input("Please input the principle amount: $"))
    apr = eval(input("Please provide the annual percentage rate: "))
    apr = apr/10
    principle = principle * (1 + apr)**10
    print("In ten years your investment will be worth:$", principle)

main()
alt()
