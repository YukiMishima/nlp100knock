f = open('hightemp.txt',encoding='utf-8')
f_prefecture = open('prefecture.txt','w',encoding='utf-8')

for line in f.readlines():
    word_list = line.split()
    prefecture_list=prefecture_list.append(word_list[0])

print(prefecture_list)