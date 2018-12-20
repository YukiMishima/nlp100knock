import re
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

r = re.compile(r'(.*?)\t(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?),(.*?)')
sentence = []
sentences = []

with open('neko.txt.mecab','r',encoding = 'utf-8_sig') as f:
    for line in f:
        if 'EOS' in line:
            if sentence:
                sentences.append(sentence)
            sentence = []
            continue
        match = r.search(line)
        if match:
            word_dict = {'surface':match.group(1),'base':match.group(8),'pos':match.group(2),'pos1':match.group(3)}
            sentence.append(word_dict)

word_list = [d['surface'] for s in sentences for d in s]
counter = Counter(word_list)

rank_appeared = np.array([i for i,s in enumerate(counter)])
# print(rank_appeared[-10:-1])
frequency_appeared = np.array([cnt for word, cnt in counter.most_common()])
x = np.log(rank_appeared)
y = np.log(frequency_appeared)

font = {'family':'IPAPGothic'}
plt.plot(x, y,'o')  # plot circle('o') not line
plt.xlabel('出現順位')
plt.ylabel('出現頻度')
plt.title('両対数プロット')
plt.show()