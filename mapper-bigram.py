#!/usr/bin/python
import sys
import re
import string

stop_words = ['a', 'able', 'about', 'across', 'after', 'all', 'almost', 'also', 'am', 'among', 'an',
              'and', 'any', 'are', 'as', 'at', 'be', 'because', 'been', 'but', 'by', 'can', 'cannot',
              'could', 'dear', 'did', 'do', 'does', 'either', 'else', 'ever', 'every', 'for', 'from',
              'get', 'got', 'had', 'has', 'have', 'he', 'her', 'hers', 'him', 'his', 'how', 'however',
              'i', 'if', 'in', 'into', 'is', 'it', 'its', 'just', 'least', 'let', 'like', 'likely', 'may',
              'me', 'might', 'most', 'must', 'my', 'neither', 'no', 'nor', 'not', 'of', 'off', 'often', 'on',
              'only', 'or', 'other', 'our', 'own', 'rather', 'said', 'say', 'says', 'she', 'should', 'since',
              'so', 'some', 'than', 'that', 'the', 'their', 'them', 'then', 'there', 'these', 'they', 'this',
              'tis', 'to', 'too', 'twas', 'us', 'wants', 'was', 'we', 'were', 'what', 'when', 'where', 'which',
              'while', 'who', 'whom', 'why', 'will', 'with', 'would', 'yet', 'you', 'your']

# This mapper function simply read text file by lines and preprocess them
# After prepricessing, this code gets neighboor pairs of words (bigrams) and print them into stdout for futrher counting

if __name__ == "__main__":

    for line in sys.stdin:
        text = line.strip()  # remove unnecessary symbols
        text = "".join([i if i not in string.punctuation else ' ' for i in text])  # remove punctuation
        text = re.sub(r'[0-9]+', '', text)  # remove numbers
        text = text.split()  # split text into individual words
        text = [i.lower() for i in text if (i.lower() not in stop_words) and (len(i) > 1)]  # remove stop-words
        for i in range(len(text) - 1):
            print(' '.join([text[i], text[i + 1]]))  # print bigrams into output
