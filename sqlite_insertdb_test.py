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
	(
		"�л�1", 1, "���� ������ 151"
	)
'''

c=conn.cursor() #��ü ����
c.execute(sql)
c.close()
conn.commit()
