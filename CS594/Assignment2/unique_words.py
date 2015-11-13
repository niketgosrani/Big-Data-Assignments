__author__ = 'Niket'

import re

stopwords = set()
allwords1 = []
allwords2 = []
special = []
special2 = []

with open('stop-word-list.txt') as f:
    for line in f:
        stopwords.add(line.rstrip('\n'))

file1 = re.findall('\w+', open('pg76.txt').read().lower())
for common in file1:
    if common not in stopwords:
        allwords1.append(common)

file2 = re.findall('\w+', open('pg74.txt').read().lower())
for common in file2:
    if common not in stopwords:
        allwords2.append(common)

for every_word in allwords1:
    if every_word not in allwords2:
        special.append(every_word)
#print len(special)

for every_word2 in allwords2:
    if every_word2 not in allwords1:
        special2.append(every_word2)
#print len(special2)

if len(special) > len(special2) :
    print 'The Adventures of Huckleberry Finn '+ 'has the highest unique words with count :' , len(special) ,'compare to The Adventures of tom sawyer which has the unique words with count :' ,len(special2)
else:
    print 'The Adventures of Tom Sawyer '+ 'has the highest unique words with count :' , len(special2),'compare to The Adventures of Huckleberry Finn which has the unique words with count :' ,len(special)


