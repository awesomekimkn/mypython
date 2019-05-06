#-*-Encoding:euc-kr-*-

from datetime import date
from datetime import datetime

boot_time=input("input boot_time as YYMMDD (example => 190101) : ")

c_year = datetime.today().year
c_month = datetime.today().month
c_day = datetime.today().day

#print(c_year)
#print(c_month)
#print(c_day)

b_year = "20" + boot_time[0:2]
b_month = boot_time[2:4]
b_day = boot_time[4:]


#print (boot_time)
#print(b_year)
#print(b_month)
#print(b_day)



d0 = date(c_year, c_month, c_day) #date 객체1
d1 = date(int(b_year), int(b_month), int(b_day)) #date 객체2
delta = d0 - d1
print ("uptime is", delta.days)

