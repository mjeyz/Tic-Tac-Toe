import random
from art import logo

print("Welcome to Tic Tac Toe Game!")

symbols = ["O", "X"]


def play_game():
    print(logo)
    print(f" {random.choice(symbols)} |   |   \n"
          f"-----------\n"
          f"   |   |   \n"
          f"-----------\n"
          f"   |   |   \n"

          )


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").upper() == "Y":
    play_game()
