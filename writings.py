import datetime
import re

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

a = open("index.htm", "r")
b = a.readlines()
c = open("input.txt", "r")
d = c.read()
e = re.sub(f"\n", f"<br> ", d)
f = '\n<div' + ' ' + 'id=\'' + timestamp + '\'>\n' + '<p style=\'font-size:10px\'>\n' + timestamp + '\n</p>\n' + '<p>\n' + e + '\n</p>\n</div>\n<br>\n\n'
b[38] += f
h = open("index.htm", "w")
h.writelines(b)
h.close()
i = open("feed.xml", "r")
l = i.readlines()
m = '\n<item>\n' + '<description>\n' + e + '\n</description>\n' + '<link>\n' + 'https://mrzgardini.github.io/writings/index.htm#' + timestamp + '\n</link>\n</item>\n\n'
l[3] += m
n = open("feed.xml", "w")
n.writelines(l)
n.close()
