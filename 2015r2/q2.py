__author__ = 'Tom'

with open ('B-small-attempt2 (1).in', 'r') as f:
    with open ('q2solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line = f.readline().split()
            N, V, X = int(line[0]), float(line[1]), float(line[2])
            faucets = []
            for i in range(N):
                next_line = f.readline().split()
                #temp first
                faucets.append([float(next_line[1]), float(next_line[0])])

            answer = ""
            if N == 1:
                if X != faucets[0][0]:
                    answer = 'IMPOSSIBLE'
                else:
                    answer = format(V/faucets[0][1], '.9f')
            if N == 2:
                faucets.sort()
                if X < faucets[0][0] or X> faucets[1][0]:
                    answer = 'IMPOSSIBLE'
                else:
                    if faucets[0][0] == faucets[1][0]:
                        answer = format(V/(faucets[0][1] +faucets[1][1]), '.9f')
                    else:
                        answer = format(max((V*(X-faucets[0][0])/(faucets[1][0]-faucets[0][0]))/faucets[1][1], (V*(faucets[1][0]-X)/(faucets[1][0]-faucets[0][0]))/faucets[0][1]), '.9f')


            solution.write('Case #' + str(case+1) + ': ' + str(answer) + '\n')



    solution.closed
f.closed