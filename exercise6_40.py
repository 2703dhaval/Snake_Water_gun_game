# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!


"""create python program and use random.choce function
game while or for loop in insert
and 10 time play
and  snake,water and gun in variable in store
user pase input levano s[snake],w[water],g[gun]
scoring karvanu and 10 var mathi jeno score vadhare hase te winner thase user or computer
"""

import random
print("welcome snake,water,gun game")
print("this game in only 10 time playing ")
game_chance = 1
you_win = 0
computer_win = 0
match_tie = 0
while(game_chance<=10):
    game = ("snake","water","gun")
    your_choice = (input(game))
    print("you enterd ,",your_choice)
    computer_choice = random.choice(game)
    print("computer enterd ,",computer_choice)
    if your_choice == computer_choice:
        print("match is tie")
        match_tie = match_tie + 1
        print(match_tie)
    elif your_choice=="snake" and computer_choice=="gun":
        print("computer win")
        computer_win = computer_win + 1
        print(computer_win)
    elif your_choice=="snake" and computer_choice=="water":
        print("you win")
        you_win = you_win + 1
        print(you_win)
    elif your_choice=="water" and computer_choice=="snake":
        print("computer win")
        computer_win = computer_win + 1
        print(computer_win)
    elif your_choice=="water" and computer_choice=="gun":
        print("you win")
        you_win = you_win + 1
        print(you_win)
    elif your_choice=="gun" and computer_choice=="snake":
        print("you win")
        you_win = you_win + 1
        print(you_win)
    elif your_choice=="gun" and computer_choice=="water":
        print("computer win")
        computer_win = computer_win + 1
        print(computer_win)
    else:
        print("check your input and try agin!")
        break
    print(10-game_chance,"time you play game")
    var = ("you win",you_win)
    var2 = ("computer win",computer_win)
    var3 = ("match tie",match_tie)
    print(var,var2,var3)
    game_chance += 1

print("game over")

if you_win==computer_win:
    print("match tie match tie point is",match_tie)
elif you_win > computer_win:
    print("you win your point is ",you_win)
else:
    print("computer win compter point is ",computer_win)









 

























     





