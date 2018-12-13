f = open('hightemp.txt',encoding='utf-8')
for line in f.readlines():
    print(line.replace('\t',' '))

