"""
@author:    Alex Oswald
@class:     DS2000
@homework:  Homework 3
@date:      04 October 2021
"""

import random

'''SAMPLE OUTPUT:
You start with $8, and a bet of $15
At the end of our simulation you have... $204
        Won:  23
        Lost: 15
        Draw: 99
[Finished in 0.15s]
'''


def craps():
    # declare variables
    BET = random.randint(5,20)  # ${5-20} per-round, constant
    money = 100  # starting
    die_1 = 0    # die 1
    die_2 = 0    # die 2
    rounds = 0   # round counter
    wins = 0     # wins counter
    loss = 0     # loss counter
    draw = 0     # draw counter

    # loop game until you run out of money or double it
    while ((money > 0) and (money < 200)):
        # initialize round (random values)
        die_1 = random.randint(1,5)
        die_2 = random.randint(1,5)
        bet = random.randint(5,20)

        # win / lose / draw conditions
        die_sum = die_1 + die_2
        if (die_sum in {7, 11}):
            wins += 1
            money += bet
        elif (die_sum in {2, 3, 12}):
            loss += 1
            money -= bet
        else:
            draw += 1
            # money unchanged

    # end game
    print("You start with $100, and a bet of $" + str(BET) + 
          "\nAt the end of our simulation you have... $" + str(money) + 
          "\n\tWon:  " + str(wins) + 
          "\n\tLost: " + str(loss) + 
          "\n\tDraw: " + str(draw))


craps()
