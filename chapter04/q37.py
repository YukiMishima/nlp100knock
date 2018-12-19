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

left = np.array([word for word, cnt in counter.most_common()[:9]])
height = np.array([cnt for word, cnt in counter.most_common()[:9]])

font = {'family':'IPAPGothic'}
# plt.title('title', **font)

# plt.rcParams['font.family'] = 'IPAPGothic'
plt.bar(left, height)
# plt.xlabel('あいうえお',**font)
plt.show()