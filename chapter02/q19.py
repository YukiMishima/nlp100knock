from collections import Counter
from operator import itemgetter

f = open('hightemp.txt', encoding = 'UTF-8')
line_list = f.readlines()

prefecture = []

for line in line_list:
    l = line.split('\t')
    prefecture.append(l[0])

#1つ目の方法
counter = Counter(prefecture)
for word, cnt in sorted(counter.items(), key = itemgetter(1), reverse = True):
    print('%s = %d 回' %(word, cnt))

#2つ目の方法
for word, cnt in counter.most_common():
    print(word, cnt)