import random
from brain import ai
import time
from functions import continue_y_n_pvc, reset_grid_pvc


# Opponent selection.
def pvc():
    print("\nYou have chosen \033[34mPlayer vs Computer\033[0m mode.\n")
    player_1 = input("Please enter your game-name: ")

    # Checking for game-name availability.
    while True:
        if player_1 == "Pinky" or player_1 == "The Brain" or player_1 == "Snowball":
            player_1 = input(f"\033[1mSorry, this name is unavailable. Please choose another one:\033[0m ")
        else:
            break

    player_1 = (f"\033[4m{player_1}\033[0m")

    # Opponent selection.
    chosen_opponent = input(f"\nAvailable opponents.\n"
                            "\033[95mp - Pinky (easy)\033[0m\n"
                            "\033[96ms - Snowball (medium)\033[0m\n"
                            "\033[93mb - The Brain (unbeatable)\033[0m\n"
                            "\n"
                            "\033[94mBonus mode: make \033[95m Pinky\033[0m \033[92mhappy\033[0m\n"                               
                            "\033[92mh - Pinky \033[0m\n"
                            "\033[94mEverytime \033[95mPinky\033[94m wins you get 1 point. If game is tied - you loose 1 point. If you win - you loose 2 points.\033[0m\n\n"
                            "Enter '\033[95mp\033[0m' ,'\033[96ms\033[0m', '\033[93mb\033[0m' or '\033[92mh\033[0m' to choose your opponent/mode: ")
    # Checking if opponent selection is correct:
    while True:
        if chosen_opponent == "p":
            player_2 = "\033[95mPinky\033[0m"
            print(f"\nYou have chosen the easy path {player_1}. Your opponent is {player_2}.\n"
                  f"I would say good luck, but I am sure you won't need it.")
            break
        elif chosen_opponent == "s":
            player_2 = "\033[96mSnowball\033[0m"
            print(f"\n{player_1} your opponent is {player_2}.\n"
                  f"Have a nice game!")
            break
        elif chosen_opponent == "b":
            player_2 = "\033[93mThe Brain\033[0m"
            print(f"\nYou have my respect {player_1} for choosing the hard path. Your opponent is {player_2}.\n"
                  f"Good luck! Because luck is your only hope.")
            break
        elif chosen_opponent == "h":
            player_2 = "\033[92mPinky\033[0m"
            print(f"\nYou have chosen \033[94mBonus mode\033[0m {player_1}. Your opponent is {player_2}.\n"
                  f"To make things more interesting,\033[92m There will be 5 rounds and you will start every as first player\033[0m.")
            time.sleep(2)
            break
        else:
            chosen_opponent = input(f"\n\033[1mThere was a problem with your entry.\033[0m\n"
                                    f"Available opponents.\n"
                                    "\033[95mp - Pinky (easy)\033[0m\n"
                                    "\033[96mp - Snowball (medium)\033[0m\n"
                                    "\033[93mb - The Brain (unbeatable)\033[0m\n"
                                    "\033[92mh - Happy \033[95mPinky \033[94m(Bonus mode)\033[0m\n"
                                    "Enter '\033[95mp\033[0m' ,'\033[96ms\033[0m', '\033[93mb\033[0m' or '\033[92mh\033[0m' to choose your opponent/mode: ")
    # Determining starting player:
    if player_2 == "\033[92mPinky\033[0m":
        player1 = player_1
    else:
        player1 = random.choice([player_1, player_2])
    if player1 == player_1:
        player2 = player_2
        player_list = [player_1, player_2]
    else:
        player2 = player_1
        player_list = [player_2, player_1]

    #Loading imitation
    if player_2 == "\033[92mPinky\033[0m":
        print("Preparing grid...")
    else:
        print("Determining the starting player...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"{player1} will start. Commencing the game..")
    time.sleep(2)
    #Setting up starting parameters for grid printing, player score and turn count
    #List for printing game grid with number choices
    listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List for checking if choices are valid, by removing all choices from the list
    listas_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List for printing game grid without number choices
    listas_ = [" ", " ", " ", "_", "_", "_", "_", "_", "_"]
    # For determining turn for current game
    turn = 1
    # For keeping track of player score
    score_1 = 0
    score_2 = 0
    # For determining turn for nex game
    player_turn = 1
    # yes/no choice simplification
    y = "\033[92my\033[0m"
    n = "\033[91mn\033[0m"
    # For The Brain move determination
    brain_list = ''
    # Starting game loop
    while True:
        # Checking starting player
        if turn % 2 == 1:
            # Symbol X/O determination
            symbol_x_o = "\033[91mX\033[0m"
            # Grid with numbers
            board2 = f"_{listas[6]}_|_{listas[7]}_|_{listas[8]}_\n_{listas[3]}_|_{listas[4]}_|_{listas[5]}_\n {listas[0]} | {listas[1]} | {listas[2]} \n"
            # Checking if turn is for computer
            if player1 == player_2:

                choice_a = ai(player_2, listas_check, brain_list, listas, symbol_x_o)

            else:
                # Player move entry
                choice_a = input(
                    f"\n{player1}, choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice: ")
            current_player = player1

        else:
            symbol_x_o = "\033[34mO\033[0m"
            board2 = f"_{listas[6]}_|_{listas[7]}_|_{listas[8]}_\n_{listas[3]}_|_{listas[4]}_|_{listas[5]}_\n {listas[0]} | {listas[1]} | {listas[2]} \n"
            if player2 == player_2:
                choice_a = ai(player_2, listas_check, brain_list, listas, symbol_x_o)
            else:
                choice_a = input(
                    f"\n{player2}, choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice: ")
            current_player = player2
        # Checking if player move entry is correct
        while True:
            if choice_a.isdigit():
                choice_a = int(choice_a)
                if choice_a in listas_check:
                    brain_list += str(choice_a)
                    break
                else:
                    print(
                        f"\033[1m{current_player}\033[1m, there was an issue with your entry. Let's try again.\033[0m")
                    time.sleep(1)
                    choice_a = input(
                        f"Choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice from available numbers/locations: ")
            else:
                print(f"\n\033[1m{current_player}\033[1m, there was an issue with your entry. Let's try again.\033[0m")
                time.sleep(1)
                choice_a = input(
                    f"Choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice from available numbers/locations: ")
        # Updating grid list according to player move entries
        listas[choice_a - 1] = symbol_x_o
        listas_[choice_a - 1] = symbol_x_o
        listas_check.remove(choice_a)
        board_ = f"_{listas_[6]}_|_{listas_[7]}_|_{listas_[8]}_\n_{listas_[3]}_|_{listas_[4]}_|_{listas_[5]}_\n {listas_[0]} | {listas_[1]} | {listas_[2]} "
        print(f"{board_}")
        time.sleep(1)
        turn += 1
        # Checking if winning condition is met
        if (listas[0] == listas[1] == listas[2]
                or listas[3] == listas[4] == listas[5] or
                listas[6] == listas[7] == listas[8] or
                listas[0] == listas[3] == listas[6] or
                listas[1] == listas[4] == listas[7] or
                listas[2] == listas[5] == listas[8] or
                listas[0] == listas[4] == listas[8] or
                listas[2] == listas[4] == listas[6]):
            # Highlighting if winning condition is met
            if listas[0] == listas[1] == listas[2]:
                board_ = (f"_{listas_[6]}_|_{listas_[7]}_|_{listas_[8]}_\n_{listas_[3]}_|_{listas_[4]}_|_{listas_[5]}"
                          f"_\n \033[7m{listas_[0]} | \033[7m{listas_[1]} | \033[7m{listas_[2]} ")
            elif listas[3] == listas[4] == listas[5]:
                board_ = (f"_{listas_[6]}_|_{listas_[7]}_|_{listas_[8]}_\n_\033[7m{listas_[3]}_|_\033[7m{listas_[4]}"
                          f"_|_\033[7m{listas_[5]}_\n {listas_[0]} | {listas_[1]} | {listas_[2]} ")
            elif listas[6] == listas[7] == listas[8]:
                board_ = (f"_\033[7m{listas_[6]}_|_\033[7m{listas_[7]}_|_\033[7m{listas_[8]}_\n_{listas_[3]}"
                          f"_|_{listas_[4]}_|_{listas_[5]}_\n {listas_[0]} | {listas_[1]} | {listas_[2]} ")
            elif listas[0] == listas[3] == listas[6]:
                board_ = (f"_\033[7m{listas_[6]}_|_{listas_[7]}_|_{listas_[8]}_\n_\033[7m{listas_[3]}_|_{listas_[4]}"
                          f"_|_{listas_[5]}_\n \033[7m{listas_[0]} | {listas_[1]} | {listas_[2]} ")
            elif listas[1] == listas[4] == listas[7]:
                board_ = (f"_{listas_[6]}_|_\033[7m{listas_[7]}_|_{listas_[8]}_\n_{listas_[3]}_|_\033[7m{listas_[4]}"
                          f"_|_{listas_[5]}_\n {listas_[0]} | \033[7m{listas_[1]} | {listas_[2]} ")
            elif listas[2] == listas[5] == listas[8]:
                board_ = (f"_{listas_[6]}_|_{listas_[7]}_|_\033[7m{listas_[8]}_\n_{listas_[3]}_|_{listas_[4]}"
                          f"_|_\033[7m{listas_[5]}_\n {listas_[0]} | {listas_[1]} | \033[7m{listas_[2]} ")
            elif listas[0] == listas[4] == listas[8]:
                board_ = (f"_{listas_[6]}_|_{listas_[7]}_|_\033[7m{listas_[8]}_\n_{listas_[3]}_|_\033[7m{listas_[4]}"
                          f"_|_{listas_[5]}_\n \033[7m{listas_[0]} | {listas_[1]} | {listas_[2]} ")
            elif listas[2] == listas[4] == listas[6]:
                board_ = (f"_\033[7m{listas_[6]}_|_{listas_[7]}_|_{listas_[8]}_\n_{listas_[3]}_|_\033[7m{listas_[4]}"
                          f"_|_{listas_[5]}_\n {listas_[0]} | {listas_[1]} | \033[7m{listas_[2]} ")
            print(f"\n{board_}")
            # Determining which player is a winner
            if player_2 == "\033[92mPinky\033[0m" and current_player == player_1:
                score_1 -= 2
                print("Pinky very not happy..")
                if score_1 <= 0:
                    score_2 = f"\033[91mSad\033[0m. Rounds left: {4 - player_turn // 2 }"
                else:
                    score_2 = f"\033[92mHappy!\033[0m. Rounds left: {4 - player_turn // 2 }"
            elif current_player == "\033[92mPinky\033[0m":
                score_1 += 1
                print("Pinky happy!!\n")
                if score_1 <= 0:
                    score_2 = f"\033[91mSad\033[0m. Rounds left: {4 - player_turn // 2 }"
                else:
                    score_2 = f"\033[92mHappy!\033[0m. Rounds left: {4 - player_turn // 2 }"
            elif current_player == player_1:
                winner = player_1
                score_1 += 1
                print(f"Congratulations {winner}, you have won this round!\n")
            else:
                score_2 += 1
                print(f"{player_2} has won this round. {player_1}, better luck next time.\n")

            print(f"Current score is:\n{player_1} : {score_1}\n{player_2} : {score_2}")
            # Inquiring to continue or to finish game with imported function
            continue_y_n_pvc(score_1, score_2, player_1, player_2, y, n, player_turn)
            # If continue - resetting grid
            listas, listas_check, listas_, turn, player1, player2, player_turn, brain_list = reset_grid_pvc(player_turn, player_list, player_2)
        # Checking for tie if grid is filled
        if len(listas_check) == 0:
            if player_2 == "\033[92mPinky\033[0m" and current_player == player_1:
                score_1 -= 1
                print("Pinky very not happy..")
                if score_1 <= 0:
                    score_2 = f"\033[91mSad\033[0m. Rounds left: {4 - player_turn // 2 }"
                else:
                    score_2 = f"\033[92mHappy!\033[0m. Rounds left: {4 - player_turn // 2 }"
            elif current_player == "\033[92mPinky\033[0m":
                score_1 -= 1
                print("Pinky not happy..")
                if score_1 <= 0:
                    score_2 = f"\033[91mSad\033[0m. Rounds left: {4 - player_turn // 2 }"
                else:
                    score_2 = f"\033[92mHappy!\033[0m. Rounds left: {4 - player_turn // 2 }"
            elif player_2 == "\033[93mThe Brain\033[0m":
                print(f"\033[1m Congrats {player_1}! It's a tie!\033[1m\n")
            elif player_2 == "\033[95mPinky\033[0m":
                print(f"\033[1m {player_2}: Yay! It's a tie!\033[1m\n")
            print(f"Current score is:\n{player1} : {score_1}\n{player2} : {score_2}")
            # Inquiring to continue or to finish game with imported function
            continue_y_n_pvc(score_1, score_2, player_1, player_2, y, n, player_turn)
            # If continue - resetting grid, switching turn order
            listas, listas_check, listas_, turn, player1, player2, player_turn, brain_list = reset_grid_pvc(player_turn, player_list, player_2)


if __name__ == "__main__":
    pvc()
