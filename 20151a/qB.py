__author__ = 'Tom'
import functools
import copy

def getkey(item):
    return item[0]

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args): # use lcmm(*list)
    """Return lcm of args."""
    return functools.reduce(lcm, args)

def myfloor(A, B): #floor A/B
    sum = 0
    total = 0
    while sum + B<  A:
        sum +=B
        total +=1
    return [total, A-sum]

with open ('B-small-practice (2).in', 'r') as f:
    with open ('Bsolution.txt', 'w') as solution:

        T = int(f.readline())
        for case in range(T):
            line1 = f.readline().split()
            B = int(line1[0])
            N = int(line1[1])
            line2 = f.readline().split()
            Ms = [int(i) for i in line2]
            lcmofM = lcmm(*Ms)
            reducedFromQueue = 0
            pplPerBarber = [0 for i in Ms]

            for i in range(len(Ms)):
                ppl = lcmofM/Ms[i]
                pplPerBarber[i] = ppl
                reducedFromQueue += ppl
            reducedN = N% reducedFromQueue

            if reducedN == 0:
                reducedN = copy.deepcopy(reducedFromQueue)
            remainingPpl = copy.deepcopy(reducedN)
            soonestnext = [None for i in range(len(Ms))]

            for i in range(len(Ms)):
                floor = myfloor(reducedN*pplPerBarber[i], reducedFromQueue)
                mydivision = floor[0]
                myremainder = floor[1]
                remainingPpl -= mydivision
                currentMinutes = (mydivision)*Ms[i]
                soonestnext[i] = [currentMinutes, i]


            soonestnext.sort(key = getkey)


            answer = soonestnext[int(remainingPpl-1)][1]
            print(remainingPpl)


            solution.write('Case #' + str(case+1) + ': ' + str(answer+1)+'\n')

    solution.closed
f.closed
