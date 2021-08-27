import random
def solution():
    door=[1,2,3]
    choose_door=random.randint(1,4)
    count=0
    while True:
        if choose_door==1:
            count+=3
            break
        elif choose_door==2:
            count+=5
            choose_door=random.randint(1,4)
        else:
            count+=7
            choose_door=random.randint(1,4)
    return count

def analysis(number_of_games:int):
    results=[]
    for i in range(number_of_games):
        results.append(solution())
    sum_results=sum(results)
    count_results=len(results)
    result=sum_results/count_results
    return result

num=1000
print(f"Average time for {num} times of playing is:",analysis(num))

    