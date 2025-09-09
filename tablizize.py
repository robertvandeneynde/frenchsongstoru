"""
// From:
A
[B]

C
[D]

// To: (html)
<table>
<tr><td>A</td><td>[B]</td></tr>
<tr><td>C</td><td>[D]</td></tr>
</table>
"""

import argparse

p = argparse.ArgumentParser()
p.add_argument('file')
args = p.parse_args()

with open(args.file, 'r', encoding='utf-8') as f:
	content = f.read()

import enum
class Modes(enum.Enum):
	OR = 1
	TR = 2
	SP = 3
	BR = 4

lines = content.splitlines()
fr, tr = [], []
mode = Modes.OR
for l in lines:
	line = l = l.strip()
	if l.startswith('['):
		assert l.endswith(']')
		expected = Modes.TR
	elif l.strip() == '':
		expected = Modes.SP
	elif l.strip() == '--':
		expected = Modes.BR
	else:
		expected = Modes.OR
	
	match expected:
		case Modes.TR:
			assert len(tr) == len(fr) - 1
			tr.append(line.strip())
		case Modes.OR:
			assert len(tr) == len(fr)
			fr.append(line.strip())
		case Modes.BR:
			assert len(tr) == len(fr)
			tr.append('')
			fr.append('')
		case Modes.SP:
			pass

with open(args.file + '.html', 'w', encoding='utf-8') as o:
	o.write('<table>')
	for a,b in zip(fr, tr, strict=True):
		o.write(f'<tr><td>{a}</td><td>{b}</td></tr>\n')
	o.write('</table>')
	print(args.file + '.html')
