#!/usr/bin/python
# First program. nomadxreborn 26/4/2018


import random


x = random.randint(1, 6)

def dice(x):
    while True:
        roll = raw_input("Press ENTER to roll the Dice!")
        x = random.randint(1, 6)
        if roll != "quit":
            print "You rolled a ", x
        elif roll == "quit":
            print "Goodbye!"
            break


dice(x)
