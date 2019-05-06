import turtle as t
import random as r

c = ["red", "white", "yellow", "blue"]
tn = ["t1", "t2", "t3", "t4"]

t.bgcolor("black")

for i in range(4):
	tn[i] = t.Turtle()
	tn[i].shape("turtle")
	tn[i].color(c[i])

	tn[i].penup()
	tn[i].goto(-300, i*80)
	tn[i].pendown()

	tn[i].pensize(5)
	tn[i].speed(1)
	tn[i].forward(r.randint(1,600))
