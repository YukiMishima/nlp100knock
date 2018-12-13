import sys
import math

f = open('hightemp.txt','r',encoding='utf-8')
lineslist = f.readlines()
args = sys.argv

num_totallines = sum(1 for line in open('hightemp.txt',encoding='utf-8'))
n= int(args[1])
num_lines = math.ceil(num_totallines/n) #切り上げ

print('分割数:',n)
print('１つのパラグラフの行数:',num_lines)

for num_paragraph in range(n):
    print(num_paragraph+1)
    offset = num_paragraph*num_lines

    for line in lineslist[offset:offset+num_lines]:
        print(line)


