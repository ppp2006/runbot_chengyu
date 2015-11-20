#encoding=utf-8

fi = open('chengyu_2col.txt', 'r')
fo = open('chengyu_2col2.txt', 'w')
index = 1
for line in fi:
    tokens = line.split(',', 2)
    if 4 == len(tokens[0].decode('utf-8')):
        fo.write('%d,%s,%s'%(index, tokens[0], tokens[1]))
        #fo.write('%s\n'%tokens[0])
        index = index +1
