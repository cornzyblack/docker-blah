import random
from colorama import Fore, Back, Style

print(Fore.RED + "some red text")
print(Back.GREEN + "and with a green background")
print(Style.DIM + "and in dim text")
print(Style.RESET_ALL)
print("back to normal now")

game_end = False
user_guess = input("Guess a color my friend?")
