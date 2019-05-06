#-*-Encoding:euc-kr-*-
import sqlite3

# TEXT -> 문자열 저장
# INTEGER -> 정수 저장용
# REAL -> 실수 저장용
# NUMERIC -> 숫자로 표현될 다른 데이터들, 날짜, 시간 등
# BLOB -> 임의 데이터 저장용 파일 (바이너리 데이터를 저장)

conn=sqlite3.connect('student.db')

sql='''
	INSERT INTO student VALUES
	(?,?,?)
'''

c=conn.cursor() #객체 생성
c.execute(sql, ('학생2', 2, '서울'))

data=[('학생3', 3, '광주'), ('학생4', 4, '대전'), ('학생5', 5, '제주'),]

c.executemany(sql,data)
c.close()
conn.commit()
