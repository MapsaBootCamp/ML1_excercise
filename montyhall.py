import random


def solution(user_choice: int, admin_choice: int, win: int):
    flag_change = 0
    # flag_win = 0
    number_of_door = [1, 2, 3]
    for i in number_of_door:
        if i == admin_choice:
            number_of_door.pop(i)
    user_choice2 = random.randint(0, 2)
    # change user input
    if user_choice2 == 0:
        user_choice2 = user_choice
        flag_change = 0
    elif user_choice2 == 1:
        for i in number_of_door:
            if i != user_choice:
                user_choice2 = i
        flag_change = 1
    # check win or lose
    if user_choice2 == win:
        flag_win = 1
    else:
        flag_win = 0
    return flag_win, flag_change


def run_number(num):
    user_choice = random.randint(1, 4)
    win = random.randint(1, 4)
    admin_choice = None

    while False:
        admin_choice = random.randint(1, 4)
        if admin_choice != user_choice and admin_choice != win:
            return True

    result_all = []
    for i in range(num):
        result_all.append(solution(user_choice, admin_choice, win))
    return result_all


def analysis(result_all: list, num):

    count_win_change = 0
    count_win_not_change = 0
    count_lose_change = 0
    count_lose_not_change = 0

    for elm in result_all:
        if elm == (1, 1):
            count_win_change += 1
        elif elm == (1, 0):
            count_win_not_change += 1
        elif elm == (0, 1):
            count_lose_change += 1
        else:
            count_lose_not_change += 1

    p_win_change = (count_win_change / num) * 100
    p_win_not_change = (count_win_not_change / num) * 100
    p_lose_change = (count_lose_change / num) * 100
    p_lose_not_change = (count_lose_not_change / num) * 100

    print("percentage of win without change:", p_win_not_change)
    print("percentage of win with change:", p_win_change)
    print("percentage of lose without change:", p_lose_not_change)
    print("percentage of lose with change:", p_lose_change)


result = run_number(1000)
analysis(result, 1000)
