print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input('choose direction "Left" or "Right":').lower()

if direction == "left":
    #Continue in game
    action =input('You come to a lake , There is an island in the middle of the lake. '
                  'Type "wait" to wait for a boat. Type "swim" to swim.').lower()
    if action == "wait":
        #Continue in game
        pick_colour = input('You are arrived at the island unharmed. '
                            'There is house with 3 doors, One red,, One yellow, and One blue,'
                            ' Which colour do you choose?').lower()
        if pick_colour == "red":
            print("Game Over.")
        elif pick_colour == "yellow":
            print("you Found the Treasure.")
        elif pick_colour == "blue":
            print("Game Over.")
        else:
            print("Game Over.")
    else:
        print("Game Over.")
if direction == "right":
    print("Game Over.")




