__author__ = 'Tom'
import itertools

def multi_choose (my_set, k):
    if k == 1:
        return [[my_set]]
    result = []
    n = len(my_set)
    for a in range(n-(k-1)):
        for a_elements in itertools.combinations(my_set, a+1):
            for choose_rest in multi_choose(my_set-set(a_elements), k-1):
                choose_rest.append(set(a_elements))
                result.append(choose_rest)
    return result


def all_partitions (list, k):
    partitions = []
    for balls_and_bins in itertools.combinations(range(len(list)-1), k-1):
        one_partition = []
        indices = [i+1 for i in balls_and_bins]
        indices.extend([0, len(list)])
        indices.sort()
        for i in range(len(indices)-1):
            one_partition.append(list[indices[i] : indices[i+1]])
        partitions.append(one_partition)
    return partitions

def nodes_in_trie(list):
    trie = set()
    for str in list:
        for i in range(len(str)+1):
            trie.add(str[:i])
    return len(trie)


with open ('D-small-practice.in', 'r') as f:
    with open ('20142q3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            line_array = f.readline().split()
            M, N = int(line_array[0]), int(line_array[1])
            S = []

            for i in range(M):
                S.append(f.readline().rstrip())

            largest = 0
            num_largest = 0

            for partition in multi_choose(set(S), N):
                total = 0
                for part in partition:
                    total += nodes_in_trie(part)
                if total > largest:
                    largest = total
                    num_largest = 1
                elif total == largest:
                    num_largest+=1

            solution.write('Case #' + str(case+1) + ': ' + str(largest) + " " + str(num_largest) + '\n')






    solution.closed
f.closed