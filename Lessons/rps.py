import random

ROCK = 1
PAPER = 2
SCISSORS = 3
def run_rps():
    det_winner(player_turn(), comp_turn())
    
def det_winner(player, comp):
    if(player > comp):
        if(player == SCISSORS and comp == ROCK):
            print("Computer wins!")
        else:
            print("You win!")
        
    if(comp > player):
        if(comp == SCISSORS and comp == ROCK):
            print("You win!")
        
        else:
            print("Computer wins!")
            

def player_turn():
    player = raw_input("rock, paper, or scissors? ")
    if(player == "rock" or player == "Rock"):
        return ROCK
    if(player == "paper" or player == "Paper"):
        return PAPER
    if(player == "scissors" or player == "Scissors"):
        return SCISSORS

def comp_turn():
    return random.randint(1,3)

run_rps()