#!/usr/bin/python
from operator import itemgetter
import sys

# Read output from mapper part and then count it in the form of dictionary.
# After this print resulting dictionary, then prints top 10 the most frequent words


count_words = dict()  # dictionary for counting
print("_________________________________________")
for line in sys.stdin:
    word = line.strip()  # remove unnecessary symbols
    try:
        count_words[word] = count_words.get(word, 0) + 1 # counter part
    except:
        continue

for word, num in count_words.items():
    print('{}\t{}'.format(word, num)) # print results

n = 0
# print 10 the most frequent words
print("TOP 10 WORDS")
for word, num in sorted(count_words.items(), key=lambda x: x[1], reverse=True):
    print('{}\t{}'.format(word, num))
    n += 1
    if n > 10:
        break
