#-*-Encoding:euc-kr-*-
import sqlite3

# TEXT -> ���ڿ� ����
# INTEGER -> ���� �����
# REAL -> �Ǽ� �����
# NUMERIC -> ���ڷ� ǥ���� �ٸ� �����͵�, ��¥, �ð� ��
# BLOB -> ���� ������ ����� ���� (���̳ʸ� �����͸� ����)

conn=sqlite3.connect('student.db')

sql='select * from student'

c=conn.cursor() #��ü ����
c.execute(sql)

#print(c.fetchone()) # �ϳ��� ���̱�

# 10���� ������ ��������
#for s in c.fetchmany(3):
#      print(s)

# ��� ������ ��������
for s in c.fetchall():
      print(s)


c.close()
conn.commit()
