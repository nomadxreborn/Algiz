
#!/usr/bin/python
# Almost complete however this version will not allow the dice to be rolled
# more than once.
import random

x = random.randint(1, 65)

def dice(x):
    while True:
        roll = raw_input("Press ENTER to roll the Dice!")
        if roll != "quit":
            print "You rolled a ", x
        elif roll == "quit":
            print "Goodbye!"
            break
dice(x)
