import datetime
import pytz
import re

timestamp = datetime.datetime.now(pytz.timezone('Europe/Rome')).strftime('%Y-%m-%d %H:%M:%S')
a = open('mrzgardini.github.io/writings/index.htm', 'r')
b = a.readlines()
c = open('writings/input.txt', 'r')
d = c.read()
o = re.sub(r"(https?://[^\s]+)", r'<a href="\1">\1</a>', d)
e = re.sub(f'\n', f'<br> ', o)
f = '\n<div class=\'data\'' + ' ' + 'id=\'' + timestamp + '\'>\n' + timestamp + '\n' + '</div>\n<div class=\'text\'>\n' + e + '\n</div>\n'
b[71] += f
h = open('mrzgardini.github.io/writings/index.htm', 'w')
h.writelines(b)
h.close()
i = open('mrzgardini.github.io/writings/feed.xml', 'r')
l = i.readlines()
m = '\n<item>\n' + '<description>\n' + '<![CDATA[' + d + ']]>' + '\n</description>\n' + '<link>\n' + 'https://mrzgardini.github.io/writings/index.htm#' + timestamp + '\n</link>\n</item>\n\n'
l[4] += m
n = open('mrzgardini.github.io/writings/feed.xml', 'w')
n.writelines(l)
n.close()
