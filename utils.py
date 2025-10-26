import random

def roll_two_d6() -> tuple[int, int]:
    cube_1 = random.randint(1,6)
    cube_2 = random.randint(1,6)

    return cube_1,cube_2

def calculates_the_dice(cubes):
    sum_cubes = 0
    for i in cubes:
        sum_cubes += i
    return sum_cubes




def closer_to_target(a: int, b: int) -> int |None:
    player_1 = a
    player_2 = b

    if player_1 > player_2:
        return 1
    elif player_2 > player_1:
        return 2
    else:
        return 3




def turn_decision() -> str:
    flag = True
    res = ""
    while flag:
        input_fn = input("please enter 'r' or 'p' : ")
        match input_fn:
            case "r":
                flag = False
                res = "r"
            case "p":
                flag = False
                res = "p"
    return res





