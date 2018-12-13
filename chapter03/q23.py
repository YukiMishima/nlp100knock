import get_uk_text as get
import re

f = get.get_uk_text().split('\n')
r = re.compile(u"(^=*)(.*?)=+$")

def word_count(word,target):
    num = 0
    if word in target:
        for character in target:
            if character == word:
                num += 1
    return num   

for line in f:
    match = r.search(line)
    if match:
        sec = match.group(2)
        level = match.group(1).count('=')-1
        print(sec, level)
        