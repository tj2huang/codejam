__author__ = 'Tom'

with open ('test.txt', 'r') as f:
    with open ('solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):

            solution.write('Case #' + str(case+1) + ': ' + str() + '\n')

