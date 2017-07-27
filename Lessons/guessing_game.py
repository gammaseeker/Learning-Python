import random as rnd

def run_game():
    minString = input("Enter lower bound: ")
    maxString = input("Enter upper bound: ")

    min = int(minString)
    max = int(maxString)

    target = get_rnd_num(min, max)
    answer = input("Enter a guess: ")
    if(int(answer) == target):
        print("Correct!")
    else:    
        while(int(answer) != target):
            print("Try again")
            answer = input("Enter a guess:")
        print("Correct!")
def get_rnd_num(min, max):
    return rnd.randint(min, max)

run_game()