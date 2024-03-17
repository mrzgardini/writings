import datetime
import pytz
import re

timestamp = datetime.datetime.now(pytz.timezone('Europe/Rome')).strftime('%Y-%m-%d %H:%M:%S')
a = open('mrzgardini.github.io/writings/index.htm', 'r')
b = a.readlines()
c = open('writings/input.txt', 'r')
d = c.read()
e = re.sub(f'\n', f'<br> ', d)
f = '\n<div' + ' ' + 'id=\'' + timestamp + '\'>\n' + '<p style=\'font-size:10px\'>\n' + timestamp + '\n</p>\n' + '<p>\n' + e + '\n</p>\n</div>\n<br>\n\n'
b[44] += f
h = open('mrzgardini.github.io/writings/index.htm', 'w')
h.writelines(b)
h.close()
i = open('mrzgardini.github.io/writings/feed.xml', 'r')
l = i.readlines()
m = '\n<item>\n' + '<description>\n' + '<![CDATA[' + d + ']]>' + '\n</description>\n' + '<link>\n' + 'https://mrzgardini.github.io/writings/index.htm#' + timestamp + '\n</link>\n</item>\n\n'
l[3] += m
n = open('mrzgardini.github.io/writings/feed.xml', 'w')
n.writelines(l)
n.close()
