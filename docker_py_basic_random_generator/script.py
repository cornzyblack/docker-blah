import random
import time
from colorama import Fore, Back

print(Fore.GREEN + "Welcome to a basic random Generator with some Colors \n")
print(
    Back.BLUE
    + "The goal of this script is to randomly generate numbers between 0 and 100 with Colors \n"
)

game_end = False


while True:
    rand_num = random.randint(0, 20)
    fore_color_to_use = random.choice(
        [
            Fore.LIGHTBLUE_EX,
            Fore.LIGHTCYAN_EX,
            Fore.LIGHTYELLOW_EX,
            Fore.LIGHTRED_EX,
            Fore.RED,
            Fore.RESET,
        ]
    )
    print(fore_color_to_use + f"Number generated: {rand_num}")

    time.sleep(5)
