import re

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
phrase = []

for s in sentences:
    tmp = ''
    step = 0
    for d in s:
        if step == 2:
            if d['pos'] == '名詞' :
                phrase.append(tmp + d['surface'])
            step = 0
            tmp = ''
        elif step == 1:
            if d['pos1'] == '連体化':
                tmp += d['surface']
                step = 2
            elif d['pos'] == '名詞':
                tmp = d['surface']
            else:
                step = 0
                tmp = ''
        elif d['pos'] == '名詞':
            tmp = d['surface']
            step = 1

print(phrase[:10])
 

