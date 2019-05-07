#-*- coding: euc-kr -*-

from datetime import date
from datetime import datetime
import re
import os
from tkinter import *

class MyApp:
	def __init__(self, Parent, text):
		self.F=Frame(Parent)
		self.F.pack()
		#self.F.title(D-Day)
		self.label1 = Label(self.F)
		self.label1["text"]=text
		self.label1.pack(side=LEFT, padx=20, pady=20)


#filename1 = "d-day.txt"
#filename2 = "hostname.txt"

c0 = os.popen('net stats')
p0 = re.compile('Ser\w+|Work\w+|ser\w+')
m0 = p0.search(c0.read())
cmd0 = m0.group()

cmd1 = 'net stats ' + cmd0
cmd2 = 'hostname'
env = os.environ['OS']

c1 = os.popen(cmd1)
c2 = os.popen(cmd2)

#def imsi_file_del():
#    os.system('del ' + filename1)
#    os.system('del ' + filename2)
#Statistics since 2/13/2019 4:11:21 PM

p = re.compile('[2][0][0-9][0-9]-[0-9]+-[0-9]+')

hostname = None

m = p.search(c1.read())

if m:
    b_year, b_month, b_day = m.group().split('-')
else: 
    p = re.compile('[0-9]+/[0-9]+/[2][0][0-9][0-9]')
    m = p.search(c1.read())
    b_month, b_day, b_year = m.group().split('/')    

hostname = c2.read()

c_year = datetime.today().year
c_month = datetime.today().month
c_day = datetime.today().day


d0 = date(c_year, c_month, c_day) #date 객체1
d1 = date(int(b_year), int(b_month), int(b_day)) #date 객체2
delta = d0 - d1

text = hostname + env + " uptime is " + str(delta.days) + " days\n" + "------ Programed by KKN ------"

root = Tk()
root.title("D-Day Print")
myapp = MyApp(root, text)

root.mainloop()

#print (hostname, env, "uptime is", delta.days, "days")
#print ("------ Programed by KKN ------")


