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

sahen_list = [word_dict['base'] for s in sentences for word_dict in s if word_dict['pos1'] == 'サ変接続']

print(sahen_list[:10])
