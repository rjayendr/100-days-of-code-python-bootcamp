# TreasureIsland.py
# This is a simple text-based adventure game where the player must navigate through choices to find treasure.
# The game starts with a welcome message and prompts the player to make choices that lead to different outcomes.
# The game is designed to be interactive and engaging, with a focus on decision-making.
WelcomeMessage = ''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
Welcome to Treasure Island.
Your mission is to find the treasure.
'''


print(WelcomeMessage)
chosenPath = input("Which path will you choose? Type 'left' or 'right': ").lower()  
match chosenPath:
    case "left":
        print("You encounter a river. Do you want to 'swim' across or 'wait' for a boat?")
        riverChoice = input().lower()
        match riverChoice:
            case "wait":
                print("You waited for a boat and crossed the river safely.")
                print("You arrive at a house with three doors: 'red', 'blue', and 'yellow'.")
                doorChoice = input("Which door will you choose? ").lower()
                match doorChoice:
                    case "red":
                        print("You entered a room full of fire. Game over.")
                    case "blue":
                        print("You entered a room full of beasts. Game over.")
                    case "yellow":
                        print("You found the treasure! You win!")
                    case _:
                        print("You chose a door that doesn't exist. Game over.")
            case "swim":
                print("You were attacked by a crocodile. Game over.")
            case _:
                print("Invalid choice. Game over.")
    case "right":
        print("You fell into a hole. Game over.")   
# This code implements a simple text-based adventure game where the player makes choices to navigate through a story.
