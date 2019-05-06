#-*-Encoding:euc-kr-*-
import sqlite3

# TEXT -> ���ڿ� ����
# INTEGER -> ���� �����
# REAL -> �Ǽ� �����
# NUMERIC -> ���ڷ� ǥ���� �ٸ� �����͵�, ��¥, �ð� ��
# BLOB -> ���� ������ ����� ���� (���̳ʸ� �����͸� ����)

conn=sqlite3.connect('student.db')

sql='''
	INSERT INTO student VALUES
	(?,?,?)
'''

c=conn.cursor() #��ü ����
c.execute(sql, ('�л�2', 2, '����'))

data=[('�л�3', 3, '����'), ('�л�4', 4, '����'), ('�л�5', 5, '����'),]

c.executemany(sql,data)
c.close()
conn.commit()
