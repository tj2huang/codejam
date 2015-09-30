__author__ = 'Tom'

MOD_VALUE = 1000002013

def calc_points(o, e, N):
    diff = e-o
    return (N*diff - diff*(diff+1)/2)%MOD_VALUE

def longest_chain (pairs):
    queue = [pairs[0]]
    furthest = pairs[0][1]
    longest = [pairs[0]]
    chain = []
    while queue:
        next = queue.pop()

        chain.append(next)
        next_endpoints = [(a,b) for (a,b) in pairs if a <= next[1]]
        if next_endpoints:
            for endpoint in next_endpoints:
                queue.append(endpoint)
        else:
            if next[1] > furthest:
                furthest = next[1]
                longest = chain[:]
            chain.pop()
    return longest


def recalc_journey(journeys, pairs, N):

    min_pair = pairs[0]
    min = journeys[min_pair]
    for pair in pairs:
        if journeys[pair] < min:
            min = journeys[pair]
            min_pair = pair
    for i in range(len(pairs)):
        if i < len(pairs)-1:
            if pairs[i][1] > pairs[i+1][0]:
                new_pair = (pairs[i+1][0], pairs[i][1])
                total = min
                if new_pair in journeys:
                    journeys[new_pair]+= total
                else:
                    journeys[new_pair] = total

        journeys[pairs[i]] -= min


    for pair in pairs:
        if journeys[pair] == 0:
            del journeys[pair]
    return (min*calc_points(pairs[0][0], pairs[-1][1], N))%MOD_VALUE





with open ('A-small-practice (2).in', 'r') as f:
    with open ('2013r2q1solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line = f.readline().split()
            N, M = int(line[0]), int(line[1])
            journeys = {}
            normal_points = 0
            for i in range(M):
                line2 = f.readline().split()
                o, e, p = int(line2[0]), int(line2[1]), int(line2[2])
                if (o, e) in journeys:
                    journeys[(o,e)] += p
                else:
                    journeys[(o, e)] = p
                normal_points += p*calc_points(o,e, N)
                normal_points = normal_points%MOD_VALUE
            reduced_points = 0
            while journeys:
                keys = list(journeys.keys())
                chain = longest_chain(sorted(keys[:]))
                reduced_points += recalc_journey(journeys, chain, N)
                reduced_points = reduced_points%MOD_VALUE
            points_cheated = (normal_points - reduced_points )% MOD_VALUE



            solution.write('Case #' + str(case+1) + ': ' + str(points_cheated) + '\n')



    solution.closed
f.closed