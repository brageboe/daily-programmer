#import matplotlib.pyplot as pyplot
#import numpy as n
import diceroller_sys

dice = "2d6"
sum_rolls = []

#print sum(diceroller_sys.diceRoller(dice))

for i in range(0,10000):
    sum_rolls.append(sum(diceroller_sys.diceRoller(dice)))
    print sum_rolls[i]

#for i in range(0, len(sum_rolls)):
