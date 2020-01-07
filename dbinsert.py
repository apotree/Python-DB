# DB 저장하기

import pymysql


conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

curs = conn.cursor()

sql = """insert into testdb.member(memID) values (%s)"""

curs.execute(sql, ('Ahn'))
curs.execute(sql, ('Seo'))

data = (('Jang'), ('Jung'))
curs.executemany(sql, data)

conn.commit()  # 실제 DB에 적용
print('추가됌')

conn.close()
