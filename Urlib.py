# Chapter 12 Classwork (Count all the words)

import urllib.request, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    # decode UTF-8
    words = line.decode().split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
