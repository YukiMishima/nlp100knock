import get_uk_text as get
import re

f = get.get_uk_text().split('\n')

regex_start = re.compile(r'{{基礎情報 ')
regex_start_field = re.compile(r'^\|')
regex_end = re.compile(r'^}}$')

basisinfo_list = {}

for line in f:
    if regex_end.match(line):
        break
    if regex_start_field.match(line):
        key, value = line.rstrip().lstrip('|').split(' = ')
        basisinfo_list[key] =  value

print(basisinfo_list)