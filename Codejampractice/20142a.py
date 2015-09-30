__author__ = 'Tom'

with open ('A-large-practice (1).in', 'r') as f:
    with open ('20142q1solution.txt', 'w') as solution:
        t = int(f.readline())

        for case in range(t):
            line = f.readline().split()
            N = int(line[0])
            X = int(line[1])
            disks = [int(x) for x in f.readline().split()]
            disks.sort()
            total = 0
            while disks:
                small = disks[0]
                if len(disks) == 1:
                    disks.pop(0)
                else:
                    smallest_complement = 0
                    for large in disks[1:]:
                        if small + large <= X:
                            smallest_complement = large
                    disks.remove(small)
                    if smallest_complement != 0:
                        disks.remove(smallest_complement)
                total+=1

            solution.write('Case #' + str(case+1) + ': ' + str(total) + '\n')


    solution.closed
f.closed
