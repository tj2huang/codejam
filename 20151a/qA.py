__author__ = 'Tom'

with open ('A-large (4).in', 'r') as f:
    with open ('Asolution.txt', 'w') as solution:

        T = int(f.readline())
        for case in range(T):
            N = int(f.readline())
            line = f.readline().split()
            totaldecrease = 0
            maxdecrease = 0
            for i in range(N):
                if i != 0:
                    if int(line[i]) < int(line[i-1]):
                        decrease = int(line[i-1]) - int(line[i])
                        totaldecrease += decrease
                        if decrease >  maxdecrease:
                            maxdecrease = decrease
            method2 = 0
            for i in range(N-1):
                if int(line[i]) < maxdecrease:
                    method2+= int(line[i])
                else:
                    method2+=maxdecrease

            solution.write('Case #' + str(case+1) + ': ' + str(totaldecrease) + ' ' + str(method2) + '\n')
    solution.closed
f.closed
