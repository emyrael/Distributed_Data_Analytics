#!/usr/bin/python
from operator import itemgetter
import sys


if __name__ == "__main__":
    count_bigrams = dict()

    print("_______________________________________")
    for line in sys.stdin:
        bigram = line.strip() # remove unnecessary symbols
        try:
            count_bigrams[bigram] = count_bigrams.get(bigram, 0) + 1 # counting part
        except:
            continue

    for bigram, num in count_bigrams.items():
        print('{}\t{}'.format(bigram, num)) # print results

    n = 0
    print("TOP 10 BIGRAMS")
    # print top 10 the most frequent words
    for bigram, num in sorted(count_bigrams.items(), key = lambda x: x[1], reverse = True):
        n+=1
        print('{}\t{}'.format(bigram, num))
        if n > 10:
            break