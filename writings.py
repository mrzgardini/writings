import datetime

o = open("index.htm", "r")
righe = o.readlines()
i = open("input.txt", "r")
righe1 = i.read()
testo = '\n<div' + ' ' + 'id=\'' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\'>\n' + '<p style=\'font-size:10px\'>\n' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n</p>\n' + '<p>\n' + righe1 + '\n</p>\n</div>\n<br>\n\n'
righe[8] += testo
o = open("index.htm", "w")
o.writelines(righe)
o.close()
