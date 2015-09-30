__author__ = 'Tom'
dic = {'11': '1', '1i': 'i', '1j': 'j', '1k': 'k',
       'i1': 'i', 'ii': '-1', 'ij': 'k', 'ik': '-j',
       'j1': 'j', 'ji': '-k', 'jj': '-1', 'jk': 'i',
       'k1': 'k', 'ki': 'j', 'kj': '-i', 'kk': '-1'
}

def mult (str1, str2):
    sign = 1
    if str1[0] == '-':
            str1 = str1[1:]
            sign *= -1
    if str2[0] == '-':
        str2 = str2[1:]
        sign *= -1
    value = dic[str1+str2]
    if value[0] == '-':
        sign *= -1
        value = value[1:]
    if sign == -1:
        value = '-' + value
    return value





with open("C-small-practice.in", "r") as f:
    with open("q3solution2.txt", "w") as solution:
        t = f.readline()
        for case in range(int(t)):
            line = f.readline()
            L = int(line.split()[0])
            X = int(line.split()[1])
            stub = f.readline()
            if stub[-1:] == "\n":
                stub = stub[:-1]
            full = stub * X
            answer = False

            check = '1'
            for i in range (L*X):
                check = mult (check, full[i])


            if check == '-1':
                first = '1'
                for a in range(L * X):
                    first = mult(first, full[a])
                    if first == 'i':
                        second = '1'
                        for b in range (a+1, L*X-1):
                            second = mult(second, full[b])
                            if second == 'j':
                                answer = True
                                break
                        if answer:
                            break
            if answer:
                text = "YES"
            else:
                text = "NO"
            solution.write('Case #' + str(case + 1) + ': ' + text + '\n')

    solution.closed
f.closed