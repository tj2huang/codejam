import math
import itertools

def check_valid(graph, ls_seating):
    valid = True
    for i in range(len(ls_seating)):
        bff = graph[ls_seating[i]]
        if bff == ls_seating[i-1] or bff == ls_seating[(i+1) % len(ls_seating)]:
            pass
        else:
            valid = False
    return valid

with open('test', 'r') as f:
    with open('q3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            N = int(f.readline())
            # 0 indexed
            largest = 0
            bff = [int(a)-1 for a in f.readline().split()]
            permutations = itertools.permutations(range(N))
            x = 1
            for perm in permutations:
                pass
                for i in reversed(range(largest, N+1)):

                    trunc = perm[:i]
                    # if check_valid(bff, trunc):
                    #     if i > largest:
                    #         largest = i

            solution.write('Case #' + str(case+1) + ': ' + str(largest) + '\n')

        solution.closed
    f.closed