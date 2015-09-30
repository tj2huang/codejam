__author__ = 'Tom'

import itertools
import math

with open ('C-small-practice.in', 'r') as f:
    with open ('q3solution.txt', 'w') as solution:
        t = int(f.readline())
        for case in range(t):
            N = int(f.readline())
            eng = set(f.readline().rstrip().split())
            fr = set(f.readline().rstrip().split())
            both = eng&fr
            not_eng_sentences = []
            not_fr_sentences = []
            eng_sentences = []
            fr_sentences = []

            for i in range(N-2):
                sentence = set(f.readline().rstrip().split())
                eng_sentences.append(sentence&eng)
                fr_sentences.append(sentence&fr)
                not_eng_sentences.append(sentence-eng)
                not_fr_sentences.append(sentence-fr)

            minimum = 99999999
            for i in range(N):
                for iter in itertools.combinations(range(N-2), i):

                    sentence_union = []
                    sentence_complement = []
                    eng_union = []
                    fr_union = []
                    for x in range(N-2):
                        if x in iter:
                            sentence_union.extend(not_eng_sentences[x])
                            eng_union.extend(eng_sentences[x])
                        else:
                            sentence_complement.extend(not_fr_sentences[x])
                            fr_union.extend(fr_sentences[x])

                    length = len(both) + len(set(eng_union)&set(fr_union)) + len(set(sentence_union)&set(sentence_complement)-both)

                    if length < minimum:
                        minimum = length

            if N==2:
                minimum = len(set(eng)&set(fr))
            print(case+1)

            solution.write('Case #' + str(case+1) + ': ' + str(minimum) + '\n')



    solution.closed
f.closed