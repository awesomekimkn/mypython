#-*-Encoding:euc-kr-*-
import sqlite3

# TEXT -> ���ڿ� ����
# INTEGER -> ���� �����
# REAL -> �Ǽ� �����
# NUMERIC -> ���ڷ� ǥ���� �ٸ� �����͵�, ��¥, �ð� ��
# BLOB -> ���� ������ ����� ���� (���̳ʸ� �����͸� ����)

conn=sqlite3.connect('student.db')

sql='''
	CREATE TABLE student
	(
		name text,
		no interger,
		addr text
	)
'''

c=conn.cursor() #��ü ����
c.execute(sql)
c.close()
