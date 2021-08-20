from random import randint

def montyhall():
    door = ['Donk' , 'Donk' , 'Donk']
    door[randint(0, 2)] = 'Benz'

    choice1 = randint(0, 2)

    host_remove = randint(0, 2)
    while host_remove == choice1 or door[host_remove] == 'Benz':

        host_remove = randint(0, 2)

    choice2 = 0
    while choice2 == host_remove or choice2 == choice1:
        choice2 = randint(0,2)

    if door[choice2] == 'Benz':

        return 'Winner'
    else:
        return 'Loser'
            
res = []
for i in range(10**6):
    res.append(montyhall())

print('Probability of Winning:', (res.count('Winner')/len(res)))
print('Probability of Loosing:', (res.count('Loser')/len(res)))