import time

# Function to determine if to finish or continue game, PvP mode.

def continue_y_n_pvp(score_1, score_2, player_1, player_2, y, n):
    """Player choice to finish game or continue"""
    continue_finish = input(f"Would you like to continue game? Press '{y}' if you do. "
                            f"Press '{n}' to finish the game: ")

    while True:
        # Option - End game = finalizing game end player scores, and exiting game
        if continue_finish == "n":
            if score_1 > score_2:
                print(f"\nCongratulations {player_1}. "
                      f"You have won this matchup with the final score - {score_1} : {score_2}."
                      f"\n{player_2}, better luck next time.")
                exit()
            elif score_1 < score_2:
                print(f"\nCongratulations {player_2}. "
                      f"You have won this matchup with the final score - {score_2} : {score_1}."
                      f"\n{player_1}, better luck next time.")
                exit()
            else:
                print(f"\nThe matchup ended in a tie with the final score - {score_2} : {score_1}."
                      f"\n{player_1} and {player_2}, thank you for participation.")
                exit()
        # Option - continue = proceeding to next match
        elif continue_finish == "y":
            break

        else:
            continue_finish = input(
                f"\033[1mSorry, could not understand your command.\033[0m\nPress '{y}' if you do. Press '{n}' to finish the game: ")


# Resting game for next mach function, for PvC mode
def reset_grid_pvc(player_turn, player_list, player_2):
    """Resetting the grid function"""
    listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listas_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listas_ = [" ", " ", " ", "_", "_", "_", "_", "_", "_"]
    turn = 1
    brain_list = ""
    if player_2 == "\033[92mPinky\033[0m":
        player_turn += 2
    else:
        player_turn += 1
    if player_turn % 2 == 1:
        player1, player2 = player_list
    else:
        player2, player1 = player_list
    print(f"\n{player1} will start next round. Resetting grid...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    return listas, listas_check, listas_, turn, player1, player2, player_turn, brain_list

# Function to determine if to finish or continue game, PvC mode.
def continue_y_n_pvc(score_1, score_2, player_1, player_2, y, n, player_turn):
    """Player choice to finish game or continue"""
    if player_2 == "\033[92mPinky\033[0m" and player_turn // 2 == 4:
        if player_2 == "\033[92mPinky\033[0m" and score_1 > 0:
            print(f"\nCongratulations {player_1}. "
                  f"You have made \033[95mPinky \033[92m Happy\033[0m. Your final score is {score_1}")
            exit()
        elif player_2 == "\033[92mPinky\033[0m" and score_1 <= 0:
            print(f"\nYou have failed {player_1}. "
                  f"\033[95mPinky \033[91mSAD\033[0m. Your final score is {score_1}")
            exit()
    else:
        continue_finish = input(f"Would you like to continue game? Press '{y}' if you do. "
                                f"Press '{n}' to finish the game: ")
    while True:
        # Option - End game = finalizing game end player scores, and exiting game
        if continue_finish == "n":
            # Other PvC
            if player_2 == "\033[92mPinky\033[0m" and score_1 > 0:
                print(f"\nAre you a quitter {player_1}? "
                      f"At least you have made \033[95mPinky \033[92m Happy\033[0m. Your final score is {score_1}")
                exit()
            elif player_2 == "\033[92mPinky\033[0m" and score_1 <= 0:
                print(f"\nYou have quit early and still failed {player_1}. "
                      f"\033[95mPinky \033[91mSAD\033[0m. Your final score is {score_1}")
                exit()
            # Happy Pinky mode
            elif score_1 > score_2 and player_2 == ("\033[95mPinky\033[0m" or "\033[96mSnowball\033[0m"):
                print(f"\nCongratulations {player_1}. "
                      f"You have won this matchup with the final score - {score_1} : {score_2}."
                      f"\n{player_2}, is devastated.")
                exit()
            elif score_1 > score_2:
                print(f"\nCongratulations {player_1}. "
                      f"You have won this matchup with the final score - {score_1} : {score_2}."
                      f"\n{player_2}, better luck next time.")
                exit()
            elif score_1 < score_2:
                print(
                    f"\n{player_2} has won this matchup with the final score - {score_2} : {score_1}."
                    f"\n{player_1}, better luck next time.")
                if player_2 == "\033[93mThe Brain\033[0m":
                    print(f"{player_2}: Finally! I can proceed with taking over the world.")
                exit()
            else:
                if player_2 == "\033[93mThe Brain\033[0m":
                    print(f"\nThe matchup ended in a tie with the final score - {score_2} : {score_1}.\n"
                          f"{player_1}, you have exceeded your expectations. Thank you for participation.")
                else:
                    print(f"\nThe matchup ended in a tie with the final score - {score_2} : {score_1}."
                          f"\n{player_1}, thank you for participation.")
                exit()
        # Option - continue = proceeding to next match
        elif continue_finish == "y":
            break
        else:
            continue_finish = input(
                f"\033[1mSorry, could not understand your command.\033[0m\nPress '{y}' if you do. Press '{n}' to finish the game: ")

# Resting game for next mach function, PvP mode.
def reset_grid_pvp(player_turn, player_list):
    """Resetting the grid function"""
    listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listas_check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listas_ = [" ", " ", " ", "_", "_", "_", "_", "_", "_"]
    player_turn += 1
    turn = 1
    if player_turn % 2 == 1:
        player1, player2 = player_list
    else:
        player2, player1 = player_list
    print(f"\n{player1} will start next round. Resetting grid...")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    return listas, listas_check, listas_, turn, player1, player2, player_turn
