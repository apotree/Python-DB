import os
import sys
import pymysql
from 1017.sqlMember import *
sqlCreateDBInit = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')

def createNodeInit():
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()

    sql = "Select Name, email, age from testdb.member1"
    curs.execute(sql, ('temp1', 'temp1@naver.com', '100'))
    curs.execute(sql, ('temp2', 'temp2@naver.com', '200'))
    curs.execute(sql, ('temp3', 'temp3@naver.com', '300'))

def createNode():
    newNode = []
    return newNode

def memberAdd() :
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()

    name = inFilter("->이름: ", 2)      #name = input("->이름: ")
    email = inFilter("->이메일: ", 2)   #email = input("->이메일: ")
    age = inFilter("->나이: ", 1)       #age = int(input("->나이: "))

    sql = """insert into testdb.member1 (name, email, age) values (%s, %s, %s) """
    curs.execute(sql, (name, email, age))

    conn.commit()
    conn.close()

def memberAllList():  #  Select절 구문 조건 없음
    print("\n-------- 회원정보 -----------")
    print("이름 \t\t 이메일 \t\t 나이")
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()

    sql = "Select Name, email, age from testdb.member1"
    curs.execute(sql)
    rows = curs.fetchall()

    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

    conn.close()

def dbConnection()
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()
    return conn, cours

def createDBInit():
    conn, curs = dbConnection()

def memberSearch():
    ser_name = inFilter = ("찾고자하는 이름 : ", 2)
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()

    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])
    conn.close()

    rows = curs.fetchall()

    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

def memberModify(memlist):
    ser_name = inFilter("찾고하고 싶은 이름:  ", 2)
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='testdb', charset='utf8')
    curs = conn.cursor()

    sql = "Select * from member1 where name=%s"
    curs.execute(sql, ser_name)

    rows = curs.fetchall()
    for row in rows:
        print(row[0], '\t', row[1], '\t', row[2])

    modiAge = input("변경할 나이 입력 > ")
    sql = """update member1 set age=%s where name=%s"""
    curs.execute(sql, modiAge, ser_name)
    print('%s님의 나이가 수정되었습니다. ' % modiAge)
    conn.commit()
    conn.close()

    for onemem in memlist:
        if ser_name in onemem:
            print("%s %s %d" % (ser_name, onemem[1], onemem[2]))
            break

    print("변경 되었음.")

def inFilter(stmt, n):
    while (True):
        if n == 1: #문자체크
            choice = input(stmt)
            if choice.isalpha() == True or choice == '': pass
            else: return int(choice)
        elif n == 2: #숫자체크
            choice = input(stmt)
            if choice.isdigit() == True or choice == '': pass
            else: return choice
        elif n == 3:  # 메뉴숫자체크
            screen()
            choice = input(stmt)
            if choice.isalpha() == True or choice == '': pass
            else: return int(choice)

def strInFilter(stmt):
    while (True):
        choice = input(stmt)
        if choice.isalpha() == True or choice == '':
            pass
        else:
            break
    return int(choice)

def intInFilter(stmt):
    while (True):
        value = input(stmt)
        if value.isdigit() == True or value == '':
            pass #os.system('cls')
        else:
            break
    return value

def menuInFilter(stmt):
    while (True):
        screen()
        choice = input(stmt)
        if choice.isalpha() == True or choice == '':
            pass
        else:
            break
    return int(choice)

def main():
    print("\n### 간단한 회원 관리 프로그램 ###")
    print("0.초기생성 1.멤버추가 2.멤버리스트 3.멤버찾기 4. 정보수정 5. 화면지우기 6.종료")

    memlist = []

    while True:
        choice = inFilter("->", 3)
        if choice == 0:
            createNodeInit()
        elif choice == 1:
            memberAdd()
        elif choice == 2:
            memberAllList()
        elif choice == 3:
            memberSearch()
        elif choice == 4:
            memberModify(memlist)
        elif choice == 5 :
            os.system("cls")
        elif choice == 6:
            sys.exit(1)
        else:
            print("잘못된 번호! 다시 입력바랍니다.")

main()