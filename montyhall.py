import random


def solution(user_choise:int,admin_choise:int,win:int):
    flag_change=0
    flag_win=0
    number_of_Door=[1,2,3]
    for i in number_of_Door:
        if i == admin_choise:
            number_of_Door.pop(i)
    user_choise2=random.randint(0,2)
    # change user iput
    if user_choise2==0:
        user_choise2=user_choise
        flag_change=0
    elif user_choise2==1:
        for i in number_of_Door:
            if i != user_choise:
                user_choise2=i
        flag_change=1
    # check win or lose
    if user_choise2==win:
        flag_win=1
    else:
        flag_win=0
    return (flag_win,flag_change)  

    

def run_number(num):
    user_choise=random.randint(1,4)
    win=random.randint(1,4)
    admin_choise=None
    
    while False:
        admin_choise=random.randint(1,4)
        if admin_choise !=user_choise and admin_choise!= win:
            return True
    
    result=[]
    for i in range(num):
        result.append(solution(user_choise,admin_choise,win))
    return result

def analysis(result:list,num):
    count_win_change=0
    count_win_notchange=0
    count_lose_change=0
    count_lose_notchange=0
    for elm in result:
        if elm == (1,1):
            count_win_change+=1
        elif elm==(1,0):
            count_win_notchange+=1
        elif elm==(0,1):
            count_lose_change+=1
        else:
            count_lose_notchange+=1

    p_win_change=(count_win_change/num)*100
    p_win_notchange=(count_win_notchange/num)*100
    p_lose_change=(count_lose_change/num)*100
    p_lose_notchange=(count_lose_notchange/num)*100
    
    print("precentage of win without change:", p_win_notchange)
    print("precentage of win with change:", p_win_change)
    print("precentage of lose without change:", p_lose_notchange)
    print("precentage of lose with change:", p_lose_change)

result=run_number(10000)
analysis(result,10000)