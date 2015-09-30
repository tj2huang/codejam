__author__ = 'Tom'

with open ('A-large.in', 'r') as f: #r is read, w is write, with ensures close even with error, simpler than try/catch
    with open ('q1solution.txt', 'w') as answer:
        t = int(f.readline())
        for case in range(t):
            line = f.readline()
            smax = int(line.split()[0])
            shyness = line.split()[1]

            sum = 0
            friends = 0

            for i in range(smax+1):
                if sum < i:
                    friends += i-sum
                    sum = i
                sum+= int(shyness[i])

            answer.write('Case #' + str(case+1) + ': '+str(friends) + '\n')


    answer.closed
f.closed