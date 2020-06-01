#ask the player to pick rock, paper, or scissors. Input this into the program
#Have the computer chose a move
#compare the choices
#see who wins from those choices

# Find a way to get random numbers.
import random

random.seed()
score = {'Player': 0, 'Computer': 0}


possible_moves = { "Rock" : "Paper",
                   "Paper" : "Scissors",
                   "Scissors" : "Rock" }


def what_score(score):
    return 'Player: {} - Computer: {}'.format(score["Player"], score["Computer"])

def get_input(possible_moves):
    valid = False
    while (not valid):
       move = input("Rock, Paper, or Scissors?\n")
       if move in possible_moves:
           valid = True
       elif move == "Exit" or move == "":
           exit()
       else:
           print("Wrong game, Doofus!\n")
    return move

def get_computer(possible_moves):
    computer = random.choice(list(possible_moves.keys()))
    print(computer)
    return computer

def is_counter(move, computer, possible_moves):
    return computer == possible_moves[move]

while True:
    # Get the input from the user
    move = get_input(possible_moves)
    # Get a move for the computer
    computer = get_computer(possible_moves)

    # Check whether someone won
    if computer == move:
        print("Nobody wins\n")
    elif is_counter(move, computer, possible_moves):
        print("You lose!\n")
        score["Computer"] = score["Computer"] + 1
    else:
        print("You win!\n")
        score["Player"] = score["Player"] + 1

    print(what_score(score))
