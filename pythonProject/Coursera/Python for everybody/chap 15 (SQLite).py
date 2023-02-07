import sqlite3
import ssl
import urllib.request, urllib.parse, urllib.error
import re


import requests

conn = sqlite3.connect('emaildb_maksim_coursera.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter adress: ')
if len(url) < 1:
    url = 'http://www.py4e.com/code3/mbox.txt'
print('Retrieving', url)
# Чтение файла txt с сайта!!!!!!
# Считал файл и записал его в файл madsv.txt
'''request_site = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urllib.request.urlopen(request_site).read().decode()

print('Retrieved', len(webpage), 'characters')
a = open("madsv.txt", "w")
a.write(webpage)
a.close()'''
a = open('madsv.txt', "r")
for line in a:
    if not line.startswith('From: '):
        continue
    pieces = line.split()
    temp = re.findall('@([\w.]+)', line)
    # print(temp)

    if len(temp) > 0:
        domain = temp[0]
        cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
        row = cur.fetchone()

        if row is None:
            cur.execute('INSERT INTO Counts(org, count) VALUES(?, 1)', (domain,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
        conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])
cur.close()