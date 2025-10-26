from utils import *
from game import *

def play_game():
    name_player_1 = input("please enter your name of player 1: ")
    name_player_2 = input("please enter your name of player 2: ")


    player_1_info = {"name": name_player_1,"score":0,"pass_count":False}
    player_2_info = {"name": name_player_2,"score":0,"pass_count":False}

    pass_flag = player_2_info["pass_count"] and player_1_info["pass_count"]

    while not pass_flag:
        print(f"turn {player_1_info["name"]}",end=" ")
        player_1_decision = turn_decision()
        if player_1_decision == "p":
            player_1_info["pass_count"] = True

        else:
            player_2_info["pass_count"] = False

            player_1_roll = roll_two_d6()
            print(f"the cube of this torn is: {player_1_roll}")
            player_1_info["score"] += calculates_the_dice(player_1_roll)
            print(f"the score of {player_1_info["name"]} is: {player_1_info["score"]} \n"
                  f"the score of {player_2_info["name"]} is: {player_2_info["score"]}" )

            if is_bust(player_1_info["score"]):
                if is_exact_100(player_1_info["score"]):
                    print(f"the winner is: {player_1_info["name"]}")
                    break
                else:
                    print(f"the winner is: {player_2_info["name"]}")
                    break


        print(f"turn {player_2_info["name"]} " ,end = "")
        player_2_decision = turn_decision()
        if player_2_decision == "p":
            player_2_info["pass_count"] = True

        else:
            player_1_info["pass_count"] = False

            player_2_roll = roll_two_d6()
            print(f"the cube of this torn is: {player_2_roll}")
            player_2_info["score"] += calculates_the_dice(player_2_roll)
            print(f"the score of {player_1_info["name"]} is: {player_1_info["score"]} \n"
                  f"the score of {player_2_info["name"]} is: {player_2_info["score"]}")


            if is_bust(player_2_info["score"]):
                if is_exact_100(player_2_info["score"]):
                    print(f"the winner is: {player_2_info["name"]}")
                    break
                else:
                    print(f"the winner is: {player_1_info["name"]}")
                    break
        pass_flag = player_2_info["pass_count"] and player_1_info["pass_count"]


    if pass_flag:
        result = closer_to_target(player_1_info["score"],player_2_info["score"])
        print("Because both players clicked 'p' the system checks whose score is higher \n"
              "if it's equal we'll move to a tie breaker")
        match result:
            case 1:
                print(f"the winner is: {player_1_info["name"]}")
            case 2:
                print(f"the winner is: {player_2_info["name"]}")
            case 3:
                print("You're in a tiebreaker, now we'll roll the dice and find out who won.")
                tie_break = tie_breaker(player_1_info["name"],player_2_info["name"])
                match tie_break:
                    case 1:
                        print(f"the winner is: {player_1_info["name"]}")
                    case 2:
                        print(f"the winner is: {player_2_info["name"]}")


if __name__ == "__main__":
    play_game()