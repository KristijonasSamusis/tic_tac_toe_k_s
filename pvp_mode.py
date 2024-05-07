import random
from functions import continue_y_n_pvp, reset_grid_pvp
import time


def pvp():
    # Player name entry
    print("\nYou have chosen \033[92mPlayer vs Player\033[0m mode.\n")
    player_1 = f"\033[4m{input("Player one, please enter your game-name: ")}\033[0m"
    player_2 = f"\033[4m{input("Player two, please enter your game-name: ")}\033[0m"
    # Checking if name are different
    while True:
        if player_1 == player_2:
            player_2 = (
                f"\033[4m{input(f"\033[1mPlayer one already has chose game-name {player_1}. Please choose another one: ")}\033[0m")
        else:
            break

    # Determining starting player:
    player1 = random.choice([player_1, player_2])
    if player1 == player_1:
        player2 = player_2
        player_list = [player_1, player_2]
    else:
        player2 = player_1
        player_list = [player_2, player_1]
    # Loading imitation
    print(f"Good luck {player_1} and {player_2}. Determining the starting player...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print(f"{player1}, you will start. Commencing the game..")
    time.sleep(2)
    # Setting up starting parameters for grid printing, player score and turn count
    # List for printing game grid with number choices
    listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # List for checking if choices are valid:
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
    # Starting game loop:
    while True:
        # Checking starting player
        if turn % 2 == 1:
            # Symbol X/O determination
            symbol_x_o = "\033[91mX\033[0m"
            # Grid with numbers
            board2 = f"_{listas[6]}_|_{listas[7]}_|_{listas[8]}_\n_{listas[3]}_|_{listas[4]}_|_{listas[5]}_\n {listas[0]} | {listas[1]} | {listas[2]} "
            # Player move entry
            choice_a = input(
                f"\n{player1}, choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice: ")
            current_player = player1

        else:
            symbol_x_o = "\033[34mO\033[0m"
            board2 = f"_{listas[6]}_|_{listas[7]}_|_{listas[8]}_\n_{listas[3]}_|_{listas[4]}_|_{listas[5]}_\n {listas[0]} | {listas[1]} | {listas[2]} "
            choice_a = input(
                f"\n{player2}, choose number/location where to place '{symbol_x_o}'.\n{board2}\nYour choice: ")
            current_player = player2
        # Checking if player move entry is correct
        while True:
            if choice_a.isdigit():
                choice_a = int(choice_a)
                if choice_a in listas_check:
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
        print(f"\n{board_}")
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
            if current_player == player_1:
                winner = player_1
                score_1 += 1
            else:
                winner = player_2
                score_2 += 1
            print(f"Congratulations {winner}, you have won this round.\n"
                  f"Current score is:\n{player_1} : {score_1}\n{player_2} : {score_2}")
            # Inquiring to continue or to finish game with imported function
            continue_y_n_pvp(score_1, score_2, player_1, player_2, y, n)
            # If continue - resetting grid
            listas, listas_check, listas_, turn, player1, player2, player_turn = reset_grid_pvp(player_turn, player_list)
        # Checking for tie if grid is filled
        if len(listas_check) == 0:
            print(f"\033[1mIt's a tie!\033[1m\n"
                  f"Current score is:\n{player1} : {score_1}\n{player2} : {score_2}")
            # Inquiring to continue or to finish game with imported function
            continue_y_n_pvp(score_1, score_2, player_1, player_2, y, n)
            # If continue - resetting grid, switching turn order
            listas, listas_check, listas_, turn, player1, player2, player_turn = reset_grid_pvp(player_turn, player_list)


if __name__ == "__main__":
    pvp()
