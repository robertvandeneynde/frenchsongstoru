import argparse
parser = argparse.ArgumentParser()
parser.add_argument('file')
args = parser.parse_args()

with open(args.file, 'r', encoding='utf-8') as f:
	content = f.read()

content = content.replace('~', '\u0303')
content = content.replace('ё-', 'е\u0304')

with open(args.file, 'w', encoding='utf-8') as f:
	f.write(content)

