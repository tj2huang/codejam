__author__ = 'Tom'

with open ('test.txt', 'r') as f:
    with open ('Asolution.txt', 'w') as solution:

        T = int(f.readline())
        for case in range(T):

            solution.write('Case #' + str(case+1) + ': ' + '\n')
    solution.closed
f.closed
