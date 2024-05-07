from pvp_mode import pvp
from pvc_mode import pvc

# Welcome message and game mode choosing
print("Welcome to the game \033[91mTic\033[0m-\033[34mTac\033[0m-Toe.")
mode = input("Available game modes:\n"
             "\033[92m1 - Player vs Player\033[0m\n"
             "\033[34m2 - Player vs Computer\033[0m\n"
             "Enter '\033[92m1\033[0m' or '\033[34m2\033[0m' to choose game mode: ")
# Checking if input is correct.
while True:
    if mode == "1":
        pvp()
    elif mode == "2":
        pvc()
    else:
        mode = input(f"\n\033[1mThere was a problem with your entry.\033[0m\n"
                     f"Available game modes:\n"
                     f"\033[92m1 - Player vs Player\033[0m\n"
                     f"\033[34m2 - Player vs Computer\033[0m\n"
                     f"Enter '\033[92m1\033[0m' or '\033[34m2\033[0m' to choose game mode: ")
