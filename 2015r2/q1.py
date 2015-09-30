__author__ = 'Tom'

import copy

def point_to(grid, r, c, dir):
    directions = ['^', 'v', '<', '>']
    if dir == '^':
        while r-1>=0:
            if grid[r-1][c] in directions:
                return (r-1, c)
            r-=1
        return False

    if dir == 'v':
        while r+1< len(grid):
            if grid[r+1][c] in directions:
                return (r+1, c)
            r+=1
        return False

    if dir == '<':
        while c-1>=0:
            if grid[r][c-1] in directions:
                return (r, c-1)
            c-=1
        return False

    if dir == '>':
        while c+1<len(grid[0]):
            if grid[r][c+1] in directions:
                return (r, c+1)
            c+=1
        return False

def fix(grid):
    total = 0

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] != '.':
                next = point_to(grid, r, c, grid[r][c])

                if not next:
                    if point_to(grid, r, c, '^') or point_to(grid, r, c, '<') or point_to(grid, r, c, '>') or point_to(grid,r, c, 'v') :
                        total +=1
                    else:
                        return 'IMPOSSIBLE'
    return total




with open ('A-large (6).in', 'r') as f:
    with open ('q1solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):

            line = f.readline().split()
            r, c = int(line[0]), int(line[1])

            grid =[ ["" for col in range(c)] for row in range(r)]
            for row in range(r):
                row_line = f.readline()
                for col in range(c):
                    grid[row][col] = row_line[col]
            answer = fix(grid)

            solution.write('Case #' + str(case+1) + ': ' + str(answer) + '\n')



    solution.closed
f.closed