#encoding=utf-8

import sys
import sqlite3

def get_idiom_info(idiom):
    db_conn = sqlite3.connect('chengyu.sqlite')
    c = db_conn.cursor()
    for row in c.execute('select * from chengyu where ChengYu = \'"%s"\'' % idiom):
    #for row in c.execute('select * from chengyu having "%s"' % idiom):
        print row[2]
    db_conn.close()
    return row[2]

if __name__ == "__main__":
    text = get_idiom_info(sys.argv[1])
    print 'result : ' + text
