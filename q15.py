import sys

f = open('merge.txt','r',encoding='utf-8')
lineslist = f.readlines()
args = sys.argv

n= int(args[1])

for line in lineslist[-n:]:
    print(line)
