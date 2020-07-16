# Assignment (Chapter 12) Follow Links in Python

import urllib.request, urllib.parse
from bs4 import BeautifulSoup

position = int(input("Position: ")) - 1
times = int(input("Times: "))
url = input("Enter URL: ")
for c in range(times):
    file = urllib.request.urlopen(url).read()
    y = BeautifulSoup(file, 'html.parser')
    findHref = y('a')
    d = findHref[position].get('href', None)
    url = d
    e = findHref[position].contents[1]
print(e)
