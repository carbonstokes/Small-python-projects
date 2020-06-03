

#import a rando number generator

import random

random.seed()
score = {'Player': 0, 'Computer': 0}

def what_score(score):
    return 'Player: {} - Computer: {}'.format(score["Player"], score["Computer"])

possible_pokemon = { "Water" : ["Fire", "Ground"],
                     "Fire" : ["Grass", "Ground"],
                     "Grass" : ["Electric", "Water"],
                     "Electric" : ["Water", "Fire"],
                     "Ground" : ["Electric", "Fire"],}

print("You have been challenged to a Pokemon battle! Choose your pokemon type:")

def get_input(possible_pokemon):
    valid = False
    while (not valid):
        player = input("Water, Fire, Grass, Electric, Ground?\n")
        if player in possible_pokemon:
            valid = True
        elif player == "Exit" or player == "":
            exit()
        else:
            print("You ran away!\n")
    return player
def get_computer(possible_pokemon):
    computer = random.choice(list(possible_pokemon.keys()))
    print(computer)
    return computer

def winner(player, computer, possible_pokemon):
    #when water is selected, it beats fire. when fire is selected is beats grass.
    # when water is selected it beats possible_pokemon["Water"]
    # When pokemon is selected it beats possible_pokemon[pokemon]
    strengths = possible_pokemon[player]
    return computer in strengths

while True:
    # Get the input from the user
    player = get_input(possible_pokemon)
    # Get a move for the computer
    computer = get_computer(possible_pokemon)

    # Check whether someone won
    if winner(player, computer, possible_pokemon):
        print("You win!\n")
        score["Player"] = score["Player"] + 1
    elif winner (computer, player, possible_pokemon):
        print("You lose!\n")
        score["Computer"] = score["Computer"] + 1
    else:
        print("Nobody wins")


    print(what_score(score))
