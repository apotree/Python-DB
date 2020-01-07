import pymysql

# DB 연결
conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
curs = conn.cursor()  # DB Table 및 결과셋에 커서 연결
sql = "select * from member"  # 실제 테이블 쿼리 문자열
curs.execute(sql)  #  curs.execute("select * from member")

# sql 문장이 실행된 후에 결과를 가져옴
rows = curs.fetchall()
for row in rows:
    print(row[0], row[1])

conn.close()
