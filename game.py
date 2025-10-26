from utils import roll_two_d6 , calculates_the_dice

def is_exact_100(score: int) -> bool:
    if score == 100:
        return True
    else:
        return False



def tie_breaker(player_1_name,player_2_name,roler :int = 0) -> int:
    flag = True
    while flag:
        player_1 = roll_two_d6()
        print(f"the cube of {player_1_name} is: {player_1}")
        score_player_1 = calculates_the_dice(player_1)

        player_2 = roll_two_d6()
        print(f"the cube of {player_2_name} is: {player_2}")
        score_player_2 = calculates_the_dice(player_2)
        if score_player_1 > score_player_2:
            roler = 1
            flag = False
        elif player_2 > player_1:
            roler = 2
            flag = False
        else:
            print("let's try again")
    return roler


def is_bust(score: int) -> bool:
    if score < 100:
        return False
    else:
        return True
