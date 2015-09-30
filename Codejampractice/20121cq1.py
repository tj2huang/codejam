__author__ = 'Tom'

import copy
with open ('A-large-practice (1).in', 'r') as f:
    with open ('2012cq1solution.txt', 'w') as solution:
        t = f.readline()
        for case in range(int(t)):
            N = int(f.readline())
            answer = 'No'
            adj = [None]*N


#adj[i][j] i inherits from j
            for i in range(N):
                line = f.readline().split()
                adj[i]= [int(x)-1 for x in line[1:]]

            for i in range(N):
                dfs = [i]
                visited = [False]*N
                while dfs:
                    current = dfs.pop(0)
                    for next in adj[current]:
                        if visited[next]:
                            answer = 'Yes'
                            dfs = []
                            break
                        else:
                            visited[next]=True
                            dfs.insert(0, next)

            solution.write('Case #' + str(case+1) + ': ' + answer + '\n')
    solution.closed
f.closed


