# dice roll generator
# NxM dice
# N = number of rolls
# M = number of sides on dice
#
# example: 2d6 means two rolls of a 6-sided dice

import sys
import random

num_rolls = input('Number of rolls: ')
num_sides = input('Number of sides on dice: ')

rolls = []

for i in range(0, num_rolls):
    # test internal state of RNG
    # if same state as previous loop -> end
    rolls.insert(i, random.randint(1,num_sides))

print sum(rolls), ': ', rolls
#print sys.argv[0] # prints script name
