import math
__author__ = 'Tom'

def addPlate(dic, key, value):
    if key not in dic:
        dic[key] = 0
    dic[key] = dic[key] + value

def calc (dic):
    heights = sorted(dic.keys())
    heights.reverse()
    tallest = heights[0]
    if tallest == 1:
        return 1
    min = tallest
    for i in range(heights[0]):
        if i > 0:
            dic2 = dic.copy()
            noOfPlates = dic2[tallest]
            del dic2[tallest]
            addPlate(dic2, i, noOfPlates)
            addPlate(dic2, tallest-i, noOfPlates)
            answer = calc(dic2)
            if answer + noOfPlates < min:
                min = answer + noOfPlates

    return min



with open('B-small-practice (2).in', 'r') as f:
    with open ('q2solution.txt', 'w') as solution:

        t = int(f.readline())
        for case in range(t):
            d = int(f.readline())
            line = f.readline()

            pis = {} # dictionary, key = pis, value = number of plates with height pi
            for pi in line.split():
                addPlate(pis, int(pi), 1)
            answer = calc(pis)
            solution.write("Case #" + str(case + 1) + ": " + str(answer) + "\n")
    solution.closed
f.closed