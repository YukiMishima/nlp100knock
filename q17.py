f = open('hightemp.txt',encoding='utf-8')
prefecture_set=set()

for line in f.readlines():
    word_list = line.split()
    prefecture_set.add(word_list[0])

print(prefecture_set)