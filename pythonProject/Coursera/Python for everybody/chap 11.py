import re

file = open("text11.txt", 'r')
result = 0
for line in file:
    y = re.findall('[0-9]+', line)
    for i in range(len(y)):
        result += int(y[i])
print(result)
