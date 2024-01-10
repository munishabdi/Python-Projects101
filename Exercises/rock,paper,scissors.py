
# Rock, Paper, Scissors:
# rock beats scissors
# scissors cuts paper
# paper covers rock

import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = None

while True:
    player = input("rock, paper, scissors: ").lower()

    if player == computer:
        print('computer', computer)
        print('player', player)
        print("Tie!")

    elif player == "rock":
        if computer == 'paper':
            print('computer', computer)
            print('player', player)
            print("You lose!")
        if computer == 'scissors':
            print('computer', computer)
            print('player', player)
            print("You win!")

    elif player == "scissors":
        if computer == 'rock':
            print('computer', computer)
            print('player', player)
            print("You lose!")
        if computer == 'paper':
            print('computer', computer)
            print('player', player)
            print("You win!")

    elif player == "rock":
        if computer == 'paper':
            print('computer', computer)
            print('player', player)
            print("You lose!")
        if computer == 'scissors':
            print('computer', computer)
            print('player', player)
            print("You win!")

    play_again = input("play again (yes/no): ").lower()
    if play_again != 'yes':
        break
print("Bye!")
