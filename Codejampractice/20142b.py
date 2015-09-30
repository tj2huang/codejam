__author__ = 'Tom'

import copy

def count_bubble (list):
    if list == None:
        return 0

    swapped = True
    total = 0
    while swapped:
        swapped = False
        for i in range(len(list)-1):
            if list[i] > list [i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                swapped = True
                total +=1
    return total

with open ('B-small-practice (3).in', 'r') as f:
    with open ('20142q2solution.txt', 'w') as solution:
        t = int(f.readline())

        for case in range(t):
            N = int(f.readline())
            a_list = [int(x) for x in f.readline().split()]
            smallest = N**2
            a_list_sorted = a_list[:]
            a_list_sorted.sort()
            index_largest = a_list.index(a_list_sorted[-1])


            for i in range(N):
                answer = 0
                #up sequence
                if i>= index_largest: #largest element is in the first part of the list
                    up_list = a_list[:i+1]
                    down_list = a_list[i+1:]
                else:
                    up_list = a_list[:i]
                    down_list = a_list[i:]
                answer += count_bubble(up_list[:])

                #down sequence
                down_list.reverse()
                answer += count_bubble(down_list[:])

                if answer < smallest:
                    smallest = answer
            solution.write('Case #' + str(case+1) + ': ' + str(smallest) + '\n')

    solution.closed
f.closed