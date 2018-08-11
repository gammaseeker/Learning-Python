import random

def roll_dice(num_times):
    for i in range (0, num_times):
        print(random.randint(1,6))

roll_dice(5)