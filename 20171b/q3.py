__author__ = 'Tom'


def solve_line(city_line, horses):
    avail = []  # list of (time, dist_remain, speed)
    c_start = 0
    c_end = len(city_line)
    avail.append([0, horses[c_start][0], horses[c_start][1]])
    for j in range(c_start, c_end):
        min_time = None
        to_remove = []
        for h_i in range(len(avail)):
            h = avail[h_i]
            if h[1] < city_line[j]:
                if not min_time:
                    min_time = h[0]
                elif h[0] < min_time:
                    min_time = h[0]
                to_remove.append(h_i)

        new_avail = []
        for i in range(len(avail)):
            if i not in to_remove:
                new_avail.append(avail[i])
        avail = new_avail
        # add switch horses
        new = []
        for h_i in range(len(avail)):
            h = avail[h_i]
            new.append([h[0], horses[j][0], horses[j][1]])
        avail.extend(new)
        if min_time:
            avail.append([min_time, horses[j][0], horses[j][1]])
        # move
        for h_i in range(len(avail)):
            h = avail[h_i]
            h[1] -= city_line[j]
            h[0] += city_line[j] / h[2]
    final_times = [h[0] for h in avail]
    return min(final_times)

# C-small-attempt0.in
with open ('test.txt', 'r') as f:
    with open ('q3solution2.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            print(case)
            line1 = f.readline().split()
            N = int(line1[0])
            Q = int(line1[1])
            horses = []
            for i in range(N):
                line2 = f.readline().split()
                ei = int(line2[0])
                si = int(line2[1])
                horses.append((ei, si))

            graph = []
            for i in range(N):
                line3 = f.readline().split()
                graph.append([int(x) for x in line3])

            # city_line = [graph[i][i+1] for i in range(N-1)]
            distances = []

            for i in range(Q):
                line4 = f.readline().split()
                c_start = int(line4[0]) - 1
                c_end = int(line4[1]) - 1

                # bfs
                q = [(c_start,[c_start], [], [horses[c_start]])]
                final_min = 9999999999999
                while q:
                    vertex, path, dist, thorses = q.pop(0)
                    con = []
                    for i2 in range(len(graph[vertex])):
                        if graph[vertex][i2] > -1:
                            con.append(i2)
                    for next in set(con) - set(path):
                        if next == c_end:
                            tempans = solve_line(dist+[graph[vertex][next]], thorses)
                            if tempans < final_min:
                                final_min = tempans
                        else:
                            q.append((next, path+[next], dist+[graph[vertex][next]], thorses+[horses[next]]))
                distances.append(final_min)
            ans = " ".join([str(x) for x in distances])

            solution.write('Case #' + str(case+1) + ': ' + ans + '\n')
