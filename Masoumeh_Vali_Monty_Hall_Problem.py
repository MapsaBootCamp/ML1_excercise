

########################################
import random
class MontyHall:
    def __init__(self):
        self.prize_door=self.pick_door()
        self.selected_door=None
        self.removed_door=None
    def pick_door(selfself):
        return random.randint(1,3)
    def select_door(selfself):
        self.selected_door=self.pick_door()
    def remove_door(selfself):
        d=self.pick_door()
        while d==self.selected_door or d==self.prize_door:
            d=self.pick_door()
        self.removed_door=d
    def switch_choice(selfself):
        self.selected_door=6-self.selected_door-self.removed_door
    def user_wins(selfself):
        if self.selected_door==self.prize_door:
            return True
        else:
            return False
    def run_game(selfself,switch=True):
        self.select_door()
        self.remove_door()
        if switch:
              self.switch_choice()
        return self.user_wins()
#####################

wins, losses=0,0
for i in range(1000):
    # make an instance of the game, call it "m"
    m=MontyHall()
    #run the game and switch choice of door
    if m.run_game(switch=True):
        #a return value of True means we've won
        wins+=1
    else:
        #a return value of False means we've lost
        losses+=1
perc_win=100.0*wins/(wins+losses)
print("\n One million Money Hall games(with switching):")
print("won:", wins, "games")
print("lost:",losses, "games")
print("odds:%.2f%% winning percentage"%perc_win)

