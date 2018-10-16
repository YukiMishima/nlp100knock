col1 = open('col1.txt','r',encoding='utf-8')
col2 = open('col2.txt','r',encoding='utf-8')
merge = open('merge.txt','w',encoding='utf-8')

for prefecture,city in zip(col1,col2):
    merge.write(prefecture.rstrip()+'\t'+city.rstrip()+'\n')

col1.close
col2.close
merge.close
