import numpy as np
import pandas as pd
import matplotlib as plt
import random


print("This is de rock, paper or scissors game. Your oponent is a AI.")
Player_name = input("Please, write your name: ")
maxPoint = int(input("How many points? \n - "))
Player = "Hello"
PlayerAI = "Hello"
Player_points = 0
PlayerAI_points = 0

while((Player_points and PlayerAI_points) < maxPoint):
    PlayerAI = random.randint(1, 3) # Rock = 1, paper = 2, scissors = 3.
    if(PlayerAI==1):
        PlayerAI = "Rock"
    elif(PlayerAI==2):
        PlayerAI = "Paper"
    elif(PlayerAI==3):
        PlayerAI = "Scissors"
    else:
        print("Error 1")

    while((Player!="Rock")and(Player!="Paper")and(Player!="Scissors")):
        Player = input("Rock, paper or scissors? \n")
        Player = Player.capitalize()
    
    print('\n', Player, ' vs ', PlayerAI)
#**********************************************Begins game**********************************************************************
    if(Player==PlayerAI):
        print("They both took out", Player, '\n')
        Player_points += 1
        PlayerAI_points += 1
        print(Player_name, ":", Player_points, "\nPlayerAI: ", PlayerAI_points, '\n')
    elif(((Player=="Rock")and(PlayerAI=="Paper"))or((Player=="Paper") and (PlayerAI=="Scissors"))or((Player=="Scissors") and (PlayerAI=="Rock"))):
        PlayerAI_points += 1
        print("PlayerAI win the point.", '\n')
        print(Player_name, ":", Player_points, "\nPlayerAI: ", PlayerAI_points, '\n')
    elif(((PlayerAI=="Rock")and(Player=="Paper"))or((PlayerAI=="Paper") and (Player=="Scissors"))or((PlayerAI=="Scissors") and (Player=="Rock"))):
        Player_points += 1
        print(Player_name, " win the point.", '\n')
        print(Player_name, ":", Player_points, "\nPlayerAI: ", PlayerAI_points, '\n')
    else:
        print("Error 2")
    
    Player = "Hello"


if((Player_points==maxPoint) and (PlayerAI_points==maxPoint)):
    print("Tie", '\n')

elif(Player_points==maxPoint):
    print(Player_name.upper(), " WIN!")
elif(PlayerAI_points==maxPoint):
    print("PlayerAI WIN!")

else:
    print("Error 3")
