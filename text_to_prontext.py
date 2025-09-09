# coding: utf-8
"""
// From:
Hello
How is life ?

// To:
Hello
[]

How is Life ?
[]
"""

from glob import glob
import re
from pathlib import Path as path
L = glob('*.txt')
i = int(input('\n'.join('{}) {}'.format(i, x) for i,x in enumerate(L)) + '\n'))
filename = L[i]
s = open(filename, encoding="utf-8").read()
o = re.sub('(\n\n|\n)', lambda m: {'\n\n': '[]\n\n--\n\n', '\n': '\n[]\n\n'}[m.group(0)], s)
P = path(outfilename := filename + '.out')
if P.exists():
	print(f'Error: file {outfilename!r} exists')
else:
	P.write_text(o)
