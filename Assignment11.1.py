#Chapter11

import re

nameF = input("Enter the name of the file")
lst = list()
sum = 0
try:
    file = open(nameF)

except:
    print("We can't find your file ")
actSum = 0
for line in file:
    x = re.findall('[0-9]+', line)
    lst = lst + x

for y in lst:
    sum = sum + int(y)

print(sum)
