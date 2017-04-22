__author__ = 'Tom'

with open ('A-large.in', 'r') as f:
    with open ('q1solutionlarge.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line = f.readline().split()
            D = int(line[0])
            N = int(line[1])
            max_time = None
            for i in range(N):
                line2 = f.readline().split()
                ki = int(line2[0])
                si = int(line2[1])
                # time i
                ti = (D-ki)/si
                if not max_time:
                    max_time = ti
                elif ti > max_time:
                    max_time = ti
            ans = D/max_time
            solution.write('Case #' + str(case+1) + ': ' + str(ans) + '\n')

