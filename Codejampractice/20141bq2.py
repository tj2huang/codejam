__author__ = 'Tom'



with open ('test.txt', 'r') as f:
    with open ('solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):

            line = f.readline().split()
            R, C, N = int(line[0]), int(line[1]), int(line[2])

            solution.write('Case #' + str(case+1) + ': ' + str() + '\n')



    solution.closed
f.closed