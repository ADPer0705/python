import random

def get_choices():
    options = ["rock", "paper", "scissors"]

    player_choice = input("Input a choice (rock, paper, scissor) : ")
    computer_choice = random.choice(options)
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices

