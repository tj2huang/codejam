__author__ = 'Tom'

def compute_one_stack(height): # naming convention: lowercase, underscore
    answer = [(0, 0)]*height #answer[i] = height i+1, (height, changes)
    for i in range(height):
        if i == 0:
            answer[i] = (1, 0)
        else:
            min = i+1
            maxheight = i+1
            minchanges = 0
            for j in range(i):
                changes = answer[i-(j+1)][1]
                changedheight = answer[i-(j+1)][0]
                finalheight = max (j+1, changedheight)
                localmin = changes +1 + finalheight
                if localmin == min:
                    if finalheight > maxheight:
                        maxheight = finalheight
                        minchanges = changes+1
                if localmin < min:
                    min = localmin
                    maxheight = finalheight
                    minchanges = changes+1

            answer[i] = (maxheight, minchanges)
    return answer

with open ('B-small-practice (2).in', 'r') as f:
    with open ('q2solution.txt', 'w') as solution:
        t = f.readline()
        answer = compute_one_stack(1000)
        print(answer)
        for case in range(int(t)):
            D = f.readline()
            line = f.readline()
            heights = line.split()
            maxim = 0
            for h in heights:
                maxim = max(maxim, answer[int(h)-1][0] + answer[int(h)-1][1])
            solution.write("Case #" + str(case+1) + ": " + str(maxim) + "\n")
    solution.closed
f.closed



