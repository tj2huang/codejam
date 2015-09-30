__author__ = 'Tom'


def calculate_entry(first, second, firstvalue, secondvalue, value):

    if first == second:  # max of all rows, cols <
        if firstvalue == secondvalue:
            value = firstvalue + matrix[row - 1][col - 1]
        elif firstvalue < secondvalue:
            value = firstvalue + matrix[row                                                                                                                         - 1][col]
            B[col - 1][0] -= firstvalue
        else:
            value = secondvalue + matrix[row][col - 1]
            A[row - 1][0] -= secondvalue
        matrix[row][col] = max(value, max(matrix[row]), max([matrix[x][col] for x in range(N + 1)]))
    else:
        matrix[row][col] = max(matrix[row][col - 1], matrix[row - 1][col])


with open ('test.txt', 'r') as f:
    with open ('20121cq3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line = f.readline().split()
            N = int(line[0])
            M = int(line[1])
            matrix = [[0 for col in range(M+1)] for row in range(N+1)] #pad with 0s
            nline = f.readline().split()
            A = [None]*N
            for i in range(N):
                A[i] = [int(nline[2*i]), int(nline[2*i+1])]
            mline = f.readline().split()
            B = [None]*M
            for i in range(M):
                B[i] = [int(mline[2*i]), int(mline[2*i+1])]

                #longest common substring
            for row in range(len(matrix)): #N+1
                for col in range(len(matrix[row])): #M+1
                    if row == 0 or col == 0:
                        matrix[row][col] = 0
                    else:
                        first = A[row - 1][1]
                        second = B[col - 1][1]
                        firstvalue = A[row - 1][0]
                        secondvalue = B[col - 1][0]
                        calculate_entry()

            maximum = 0
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    if matrix[row][col]> maximum:
                        maximum = matrix[row][col]

            solution.write('Case #' + str(case+1)+ ': '+ str(maximum) + '\n')
    solution.closed
f.closed




