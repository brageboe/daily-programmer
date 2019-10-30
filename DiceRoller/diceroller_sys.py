# dice roll generator
# NdM dice
#
# example: 2d6 means two rolls of a 6-sided dice

import sys
import random

def argvCheck(argv):
    if argv.count('d'):
        [nrolls, nsides] = argv.split('d')
        if nrolls.isdigit() & nsides.isdigit():
            return int(nrolls), int(nsides)
    sys.exit("Invalid input argument; must have form 'NdM' where N,M are integers")

def diceRoller(argv):
    [num_rolls, num_sides] = argvCheck(argv)
    rolls = []

    for i in range(0, num_rolls):
        rolls.insert(i, random.randint(1,num_sides))

    return rolls

if __name__ == "__main__":
    rolls = diceRoller(sys.argv[1])
    print sum(rolls), ': ', rolls
