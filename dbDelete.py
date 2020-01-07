import pymysql

modiID = input('지울 ID : ')

conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
curs = conn.cursor()

sql = """Delete from member where memID=%s"""
curs.execute(sql, modiID)

conn.commit()

print('삭제완료')

conn.close()
