import math
import itertools


def check_valid(graph, ls_seating):
    valid = True
    for i, val in enumerate(ls_seating):
        bff = graph[val]
        if not (bff == ls_seating[i-1] or bff == ls_seating[(i+1) % len(ls_seating)]):
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
            for i in range(1, N+1):
                permutations = itertools.permutations(range(N), r=i)
                for perm in permutations:
                    if check_valid(bff, perm):
                        if i > largest:
                            largest = i

            solution.write('Case #' + str(case+1) + ': ' + str(largest) + '\n')

        solution.closed
    f.closed