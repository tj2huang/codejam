import math
__author__ = 'Tom'

def addPlate(dic, key, value):
    if key not in dic:
        dic[key] = 0
    dic[key] = dic[key] + value


with open('B-small-attempt1.in', 'r') as f:
    with open ('q2solution.txt', 'w') as solution:

        t = int(f.readline())
        for case in range(t):
            d = int(f.readline())
            line = f.readline()

            pis = {} # dictionary, key = pis, value = number of plates with height pi
            for pi in line.split():
                addPlate(pis, int(pi), 1)


            numberStacksHalved = 0
            totalStacksHalved = 0
            heights = sorted(pis.keys())
            heights.reverse()
            highestStackAfterHalving = heights[0]
            worth = False

            while heights[0]>1: #go through plates from tallest to shortest, while the tallest stack taller than 1
                pi = heights[0]
                numPlates = pis[pi]
                numberStacksHalved += numPlates
                del pis[pi]
                addPlate (pis, math.ceil(pi/2), numPlates)
                addPlate (pis, math.floor(pi/2), numPlates)
                heights = sorted(pis.keys())
                heights.reverse()
                if pi - heights[0] > numberStacksHalved: #worth
                    highestStackAfterHalving = heights[0]
                    totalStacksHalved += numberStacksHalved
                    numberStacksHalved = 0
            solution.write("Case #" + str(case + 1) + ": " + str(highestStackAfterHalving+totalStacksHalved) + "\n")
    solution.closed
f.closed










