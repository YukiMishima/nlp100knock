from operator import itemgetter

with open('hightemp.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

def is_float(s):
    try:
        float(s)
    except ValueError:
        return str(s)
    else:
        return float(s)

s_list = []
line_list = []

for line in lines:
    line = line.split('\t')
    s_list = [is_float(s) for s in line]
    line_list.append(s_list)

print(sorted(line_list, key = itemgetter(2) ,reverse=False))
