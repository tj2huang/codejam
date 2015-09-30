__author__ = 'Tom'

with open('test.txt', 'r') as f:
    with open ('Bsolution.txt', 'w') as solution:

        T = int(f.readline())
        for case in range(T):
            line1 = f.readline().split()
            B = int(line1[0])
            N = int(line1[1])
            line2 = f.readline().split()
            Ms = [int(i) for i in line2]
            low, high = -1, max(Ms)*N



