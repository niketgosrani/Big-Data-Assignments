import collections
import operator
import re
import csv

stopwords = set()
allwords = []


with open('stop-word-list.txt') as f:
    for line in f:
        stopwords.add(line.rstrip('\n'))
        # print stopwords

file = re.findall('\w+', open('pg174.txt').read().lower())
for line in file:
    if line not in stopwords:
        allwords.append(line)

wordcount = {}
for word in allwords:
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

#print collections.Counter(allwords).most_common(100)

sorted_x = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
#for k, v in sorted_x:
    #print k, ':', v
print '\nHighest occurring element is', sorted_x[0]

with open('data.csv', 'w') as f:
        for k, v in sorted_x:
                f.write(k + ',' + str(v) + '\n')



