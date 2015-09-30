__author__ = 'Tom'

table = {'11': '1', '1i': 'i', '1j': 'j', '1k': 'k',
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
    value = table[str1+str2]
    if value[0] == '-':
        sign *= -1
        value = value[1:]
    if sign == -1:
        value = '-' + value
    return value

with open('C-large-practice.in', 'r') as f:
    with open ('q3solution.txt', 'w') as solution:
        t = f.readline()
        for case in range(int(t)):
            line = f.readline()
            L = int(line.split()[0])
            X = int(line.split()[1])
            string = f.readline()
            if string[-1:] == "\n":
                string = string[:-1]
            answer = False
            Lmult = '1'
            powers = ['1']*4
            for i in range(L):
                Lmult = mult(Lmult,string[i])
            for i in range(4):
                if i == 0:
                    powers[0] = Lmult
                else:
                    powers[i] = mult(Lmult, powers[i-1])
            #check that all of it multiplies to -1
            if powers[(X-1)%4] == '-1':
                first = '1'
                for firstend in range (L): # multiply for first segment, mult by 4 to account for power of 4?
                    if answer:
                        break
                    first = mult(first, string[firstend])
                    for firstpower in range (4):
                        if mult(first, powers[firstpower]) == 'i':
                            second = '1'
                            for secondend in range(L):
                                if answer:
                                    break
                                second = mult(second, string[(secondend +1 + firstend)%L])
                                for secondpower in range(4):
                                    if mult(second, powers[secondpower]) == 'j':
                                        #verify sum of powers and digits checks out
                                        totalL = 1
                                        if firstend + 1 + secondend + 1 >=L :
                                            totalL += 1
                                        totalL += (firstpower+1)%4 + (secondpower+1)%4
                                        if totalL <= X:
                                            answer = True


            if answer:
                text = "YES"
            else:
                text = "NO"
            solution.write('Case #' + str(case + 1) + ': ' + text + '\n')

    solution.closed
f.closed

