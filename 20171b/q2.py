__author__ = 'Tom'


def sol(N, n_col):
    m = max(n_col)
    if m > N//2:
        return "IMPOSSIBLE"
    basic = [n_col[0], n_col[2], n_col[4]]
    code = ['R', 'Y', 'B']
    i_max = basic.index(m)
    fill = [""]*(m+1)
    ponies = []
    for i in range(3):
        if i != i_max:
            ponies.extend([code[i]]*basic[i])

    for i in range(len(ponies)):
        fill[i%(m+1)] += ponies[i]
    return code[i_max].join(fill)

with open ('B-small-attempt0.in', 'r') as f:
    with open ('q2solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line = f.readline().split()
            N = int(line[0])
            n_col = []
            for i in range(6):
                n_col.append(int(line[i+1]))
            ans = sol(N, n_col)
            solution.write('Case #' + str(case+1) + ': ' + ans + '\n')

