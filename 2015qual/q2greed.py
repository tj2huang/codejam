__author__ = 'Tom'
import math
import time
#note: math.ceil takes 4 billion years
with open ('B-large-practice (1).in', 'r') as f:
    with open ('q2solutiongreed.txt', 'w') as solution:
        t = f.readline()
        for case in range(int(t)):
            D = int(f.readline())
            line = f.readline()
            heights = [int(height) for height in line.split()]
            print (heights)
            max = 0
            for pile in heights:
                if pile > max:
                    max = pile
            minutes = max
            for tallest in range(1, max+1):
                moves = tallest
                for pile in heights:
                    moves += math.ceil(pile/tallest) -1
                if moves < minutes:
                    minutes = moves
            solution.write('Case #' + str(case+1) + ': ' + str(minutes) + '\n')


    solution.closed
f.closed