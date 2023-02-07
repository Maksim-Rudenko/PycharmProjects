import json
import urllib.request, urllib.parse, urllib.error

#http://py4e-data.dr-chuck.net/comments_1614406.json
url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
print('Count:', len(info['comments']))

sum = 0
for item in info['comments']:
    sum += int(item['count'])
print('Sum:', sum)