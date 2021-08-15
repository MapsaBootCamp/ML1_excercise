import random


door_with_prize = random.randint(0, 2)
first_choice = random.randint(0, 2)

def first_round():
    doors = [0, 1, 2]
    for i in doors:
        if i == door_with_prize:
            if first_choice == door_with_prize:
                doors.remove(i)
                shown_door = random.choice(doors)
            else:
                doors.remove(i)
                doors.remove(int(first_choice))
                shown_door = doors[0]
            return shown_door


def switch_door():
    doors = [0, 1, 2]
    doors.remove(first_round())
    choice = random.randint(0, 1)
    if choice == 0:
        second_choice = first_choice
    else:
        doors.remove(int(first_choice))
        second_choice = doors[0]
    return second_choice


count = 0
n_max = 50
n = 50
while n > 0:
    if int(switch_door()) == door_with_prize:
        count += 1
    n -= 1

print(count / n_max)